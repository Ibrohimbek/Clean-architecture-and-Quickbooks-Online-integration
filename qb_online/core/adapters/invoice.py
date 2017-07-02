from typing import Iterable, Dict, Optional, NamedTuple

from qb_online.core.repositories.invoice_repository import InvoiceRepository
from qb_online.core.use_cases.invoice_use_case import InvoiceUseCase

from qb_online.core.entities.invoice import Invoice


class InvoiceLineData(NamedTuple):
    description = ''
    net_value = ''


class InvoiceData(NamedTuple):
    number = ''
    lines = Iterable[InvoiceLineData]


class InvoiceAdapter:

    def __init__(self, repository: InvoiceRepository):
        self.use_case = InvoiceUseCase(repository)

    def get_list(self, filters: Optional[Dict[str, str]]) -> Iterable[InvoiceData]:
        invoices = self.use_case.get_list(filters)
        invoices_data = []
        for invoice in invoices:
            invoices_data.append(self._invoice_to_data(invoice))
        return invoices_data

    def create(self, invoice_data: InvoiceData) -> InvoiceData:
        invoice = self._data_to_invoice(invoice_data)
        invoice = self.use_case.create(invoice)
        return self._invoice_to_data(invoice)

    @classmethod
    def _invoice_to_data(cls, invoice: Invoice) -> InvoiceData:
        pass

    @classmethod
    def _data_to_invoice(cls, invoice_data: InvoiceData) -> Invoice:
        pass
