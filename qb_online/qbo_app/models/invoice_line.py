import uuid

from django.db import models

from .base import BaseModel


class InvoiceLine(BaseModel):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    invoice = models.ForeignKey('qbo_app.Invoice', related_name='lines')

    service_item = models.ForeignKey('qbo_app.ServiceItem', related_name='invoice_lines', blank=True)
    description = models.CharField(max_length=200)
    quantity = models.DecimalField(max_digits=10, decimal_places=2, default=1, blank=True)
    rate = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    class Meta:
        ordering = ('id',)
        verbose_name_plural = 'Invoice lines'

    def __str__(self):
        return self.description
