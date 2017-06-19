from typing import Iterable

from qb_online.core.entities.invoice import Invoice


class InvoiceRepository:

    def get_list(self, filters) -> Iterable[Invoice]:
        raise NotImplementedError()

    def save(self, invoice: Invoice) -> Invoice:
        raise NotImplementedError()

    # def atomic(self) -> ContextManager:
    #     raise NotImplementedError()
