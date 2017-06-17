import uuid

from django.db import models

from .base import BaseModel


class Order(BaseModel):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    load_id = models.CharField('Load ID', max_length=100)
    payment_term = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        ordering = ['changed_at']
