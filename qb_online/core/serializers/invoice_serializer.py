import json


class InvoiceEncoder(json.JSONEncoder):

    def default(self, invoice):
        try:
            to_serialize = {
                'uid': invoice.uid,
                'number': invoice.number,
                'invoiced_date': invoice.invoiced_date,
                'order': invoice.order,
                'customer': invoice.customer,
                'payment_term': invoice.payment_term,
            }
            return to_serialize
        except AttributeError:
            return super().default(invoice)
