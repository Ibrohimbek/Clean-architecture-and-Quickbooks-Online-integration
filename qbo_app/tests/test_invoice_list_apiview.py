# import json
# from unittest import mock
#
# from rest_framework.test import APITestCase
#
# from core.domain.invoice import Invoice
# from core.shared import response_object as res
#
#
# class InvoiceListGetAPITestCase(APITestCase):
#     def setUp(self):
#         self.invoice_1_dict = {
#             'uid': 'f853578c-fc0f-4e65-81b8-566c5dffa35a',
#             'number': 1, 'invoiced_date': '2017-05-20',
#             'order': 2, 'customer': 3, 'payment_term': 4
#         }
#
#         self.invoice1_domain_model = Invoice.from_dict(self.invoice_1_dict)
#
#         self.invoices = [self.invoice1_domain_model]
#
#     @mock.patch('core.use_cases.invoice_use_case.InvoiceListUseCase')
#     def test_get(self, mock_use_case):
#         mock_use_case().execute.return_value = res.ResponseSuccess(self.invoices)
#
#         http_response = self.client.get('/invoices/')
#
#         assert json.loads(http_response.data.decode('UTF-8')) == [self.invoice_1_dict]
#         assert http_response.status_code == 200
#         assert http_response.mimetype == 'application/json'
