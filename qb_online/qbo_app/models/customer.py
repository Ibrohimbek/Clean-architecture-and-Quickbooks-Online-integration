import uuid

from django.db import models

from .base import BaseModel


class Customer(BaseModel):
    company = models.ForeignKey('qbo_app.Company', related_name='customers')

    uid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    qbo_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)

    address = models.CharField(max_length=250)
    email = models.CharField(max_length=100)
    fax = models.CharField(max_length=100)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Customers'

    def __str__(self):
        return self.name