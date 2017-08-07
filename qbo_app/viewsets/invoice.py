# import json
#
# from core.adapters.invoice import InvoiceAdapter
# from core.repositories.invoice_repository import InvoiceRepository
# from rest_framework.views import APIView
#
#
# class InvoiceViewSet(APIView):
#     def __init__(self, *args, **kwargs):
#         self.super().__init__(*args, **kwargs)
#
#         self.adapter = InvoiceAdapter(InvoiceRepository())
#
#     def get(self, number=None):
#         if number:
#             return self.get_one(number)
#         return self.get_list()
#
#     def get_one(self, number):
#         invoice = self.adapter.get_list({'number': number})
#         return json.dumps(invoice)
#
#     def get_list(self):
#         invoices = self.adapter.get_list()
#         return json.dumps(invoices)
