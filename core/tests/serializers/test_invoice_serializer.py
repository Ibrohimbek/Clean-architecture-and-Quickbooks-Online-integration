import json

from core.domain.invoice import Invoice
from core.serializers.invoice_serializer import InvoiceEncoder


def test_serialize_entity_invoice():
    uid = 'f853578c-fc0f-4e65-81b8-566c5dffa35a'

    invoice = Invoice(uid=uid, number=1, invoiced_date='2017-05-20', order=2, customer=3, payment_term=4)

    expected_json = """
        {
            "uid": "f853578c-fc0f-4e65-81b8-566c5dffa35a",
            "number": 1,
            "invoiced_date": "2017-05-20",
            "order": 2,
            "customer": 3,
            "payment_term": 4
        }
    """

    assert json.loads(json.dumps(invoice, cls=InvoiceEncoder)) == json.loads(expected_json)
