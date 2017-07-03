from core.domain import invoice


class InvoiceRepository:

    def __init__(self, entries=None):
        self._entries = []

        if entries:
            self._entries.extend(entries)

    def _check(self, element, key, value):
        if '__' not in key:
            key = key + '__eq'

        key, operator = key.split('__')

        if operator not in ['eq', 'lt', 'gt']:
            raise ValueError('Operator {} is not supported'.format(operator))

        operator = '__{}__'.format(operator)

        return getattr(element[key], operator)(value)

    def list(self, filters=None):
        if not filters:
            return self._entries

        result = []
        result.extend(self._entries)

        for key, value in filters.items():
            result = [e for e in result if self._check(e, key, value)]

        return [invoice.Invoice.from_dict(r) for r in result]


# from typing import Iterable
#
# class InvoiceRepository:
#
#     def get_list(self, filters) -> Iterable[Invoice]:
#         raise NotImplementedError()
#
#     def save(self, invoice: Invoice) -> Invoice:
#         raise NotImplementedError()
#
#     # def atomic(self) -> ContextManager:
#     #     raise NotImplementedError()
#
