# from typing import Iterable, Dict, Optional
#
# from core.repositories.invoice import InvoiceRepository
# from core.entities.invoice import Invoice

from core.shared import response_object as res
from core.shared import use_case as uc


class InvoiceListUseCase(uc.UseCase):

    def __init__(self, repository):
        self.repository = repository

    def process_request(self, request_object):
        domain_storageroom = self.repository.list(filters=request_object.filters)
        return res.ResponseSuccess(domain_storageroom)


# class InvoiceUseCase:
#
#     def __init__(self, repository: InvoiceRepository):
#         self.repository = repository
#
#     def get_list(self, filters: Optional[Dict[str, str]]) -> Iterable[Invoice]:
#         return self.repository.get_list(filters)
#
#     def create(self, invoice: Invoice) -> Invoice:
#
#         for line in invoice.lines:
#             line.validate()
#         invoice.validate()
#
#         with self.repository.atomic():
#             self._validate_invoice_number(invoice)
#             invoice = self.repository.save(invoice)
#
#         return invoice
#
#     def _validate_invoice_number(self, invoice: Invoice):
#         pass
