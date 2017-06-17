from django.db import models

from .managers import SafeRemovableManager, BaseManager, cascade_deactivate, cascade_activate


class BaseModel(models.Model):
    is_removed = models.BooleanField(default=False, db_index=True)

    created_at = models.DateTimeField(auto_now_add=True, blank=False)
    changed_at = models.DateTimeField(auto_now=True, blank=False)

    objects = SafeRemovableManager()
    all_objects = BaseManager()

    class Meta:
        abstract = True
        ordering = ('-changed_at',)

    def save(self, *args, **kwargs):
        update_fields = kwargs.get('update_fields', None)
        if update_fields and 'changed_at' not in update_fields:
            update_fields.append('changed_at')

        super(BaseModel, self).save(*args, **kwargs)

    def delete(self, using=None, force=False, cascade=True):
        if force:
            super(BaseModel, self).delete(using)
        else:
            if cascade:
                cascade_deactivate(self, using)
            else:
                self.is_removed = True
                self.save(update_fields=['is_removed'])

    def restore(self):
        self.is_removed = False
        self.save(update_fields=['changed_at', 'is_removed'])

    def cascade_activate(self):
        cascade_activate(self)

