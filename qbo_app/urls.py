from django.conf.urls import url

from .views.invoice_list_view import InvoiceListAPIView

urlpatterns = [
    url(r'^invoices/$', InvoiceListAPIView.as_view(), name='invoices-list'),
]
