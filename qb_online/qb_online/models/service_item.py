import uuid

from django.db import models

from .base import BaseModel


class ServiceItem(BaseModel):
    company = models.ForeignKey('qb_online.Company', related_name='service_items')

    uid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    qbo_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
