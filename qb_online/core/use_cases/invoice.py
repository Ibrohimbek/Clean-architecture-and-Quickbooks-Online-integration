from typing import Iterable, Dict, Optional

from qb_online.core.repositories.invoice import InvoiceRepository
from qb_online.core.entities.invoice import Invoice


class InvoiceUseCase:

    def __init__(self, repository: InvoiceRepository):
        self.repository = repository

    def get_list(self, filters: Optional[Dict[str, str]]) -> Iterable[Invoice]:
        return self.repository.get_list(filters)

    def create(self, invoice: Invoice) -> Invoice:

        for line in invoice.lines:
            line.validate()
        invoice.validate()

        with self.repository.atomic():
            self._validate_invoice_number(invoice)
            invoice = self.repository.save(invoice)

        return invoice

    def _validate_invoice_number(self, invoice: Invoice):
        pass