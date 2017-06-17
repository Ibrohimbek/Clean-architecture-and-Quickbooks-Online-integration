import uuid

from django.db import models

from .base import BaseModel


class Invoice(BaseModel):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    order = models.ForeignKey('qbo_app.Order', related_name='invoices')

    invoice_number = models.CharField('Invoice Number', max_length=11, blank=True)
    invoice_date = models.DateTimeField('Invoice Date')

    customer = models.ForeignKey('qbo_app.Customer', related_name='invoices')
    payment_term = models.CharField('Term name', max_length=100, blank=True)

    # Result information
    txn_id = models.CharField('Txn ID', max_length=36, blank=True)
    txn_number = models.IntegerField('Txn Number', blank=True, null=True)

    is_synced = models.NullBooleanField('Is created in QBO')
    message = models.CharField('Message', max_length=255, blank=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return '{}/{}'.format(self.invoice_number, self.invoice_date)

