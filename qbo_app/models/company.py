import uuid

from django.db import models

from .base import BaseModel


class Company(BaseModel):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=100, db_index=True)

    connected = models.BooleanField(default=False)

    realm_id = models.BigIntegerField(blank=True, null=True)
    token = models.CharField(max_length=100, blank=True, null=True)
    secret = models.CharField(max_length=100, blank=True, null=True)
    token_updated_at = models.DateTimeField(blank=True, null=True)

    default_item_id = models.IntegerField(blank=True, null=True)
    default_item_name = models.CharField(max_length=200, blank=True, null=True)

    default_taxcode_id = models.CharField(max_length=50, blank=True, null=True)
    default_taxcode_name = models.CharField(max_length=100, blank=True, null=True)

    country = models.CharField(max_length=100, default='US', null=True)

    class Meta:
        ordering = ['name']

    def qb_disconnect(self):
        self.connected = False
        self.save()

    def is_us_company(self):
        return self.country.lower() == 'us'
