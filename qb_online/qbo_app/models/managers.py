from django.contrib.admin.utils import NestedObjects
from django.contrib.auth.base_user import BaseUserManager
from django.db import DEFAULT_DB_ALIAS, models
from django.utils import timezone


class BaseQuerySet(models.QuerySet):
    def delete(self, force=False, cascade=True):
        if force:
            super(BaseQuerySet, self).delete()
        else:
            if cascade:
                for obj in self:
                    cascade_deactivate(obj)
            else:
                self.update(is_removed=True)

    def cascade_activate(self):
        for obj in self:
            cascade_activate(obj)


def cascade_deactivate(obj, using=None):
    if using is None:
        using = DEFAULT_DB_ALIAS
    collector = NestedObjects(using)
    collector.collect([obj])
    deactivate(collector.nested())


def deactivate(objects):
    for obj in objects:
        if isinstance(obj, list):
            deactivate(obj)
        else:
            if hasattr(obj, 'is_removed'):
                obj.is_removed = True
                obj.save(update_fields=['changed_at', 'is_removed'])
            else:
                obj.delete()


def cascade_activate(obj, using=None):
    if using is None:
        using = DEFAULT_DB_ALIAS

    collector = NestedObjects(using)
    collector.collect([obj])

    activate(collector.nested())


def activate(objects):
    for obj in objects:
        if isinstance(obj, list):
            activate(obj)
        else:
            obj.restore()


BaseManager = models.Manager.from_queryset(BaseQuerySet)


class SafeRemovableManager(BaseManager):
    _queryset_class = BaseQuerySet

    def get_queryset(self):
        kwargs = {'model': self.model, 'using': self._db}
        if hasattr(self, '_hints'):
            kwargs['hints'] = self._hints

        return BaseQuerySet(**kwargs).filter(is_removed=False)


class UserManager(BaseUserManager, BaseManager):
    def _create_user(self, email, password, is_admin=False, is_staff=True, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)
        user = self.model(email=email, is_admin=is_admin, is_staff=is_staff, last_login=timezone.now(), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, is_admin=True, **extra_fields)


class SoftRemovableUserManager(UserManager):
    _queryset_class = BaseQuerySet

    def get_queryset(self):
        kwargs = {'model': self.model, 'using': self._db}
        if hasattr(self, '_hints'):
            kwargs['hints'] = self._hints

        return BaseQuerySet(**kwargs).filter(is_removed=False)
