import uuid
from datetime import datetime

from core.domain.invoice import Invoice


def test_invoice_entity_init():
    uid = uuid.uuid4()
    current_date = datetime.now().today()

    invoice = Invoice(uid=uid, number=1, invoiced_date=current_date, order=2, customer=3, payment_term=4)

    assert invoice.uid == uid
    assert invoice.number == 1
    assert invoice.invoiced_date == current_date
    assert invoice.order == 2
    assert invoice.customer == 3
    assert invoice.payment_term == 4


def test_invoice_entity_from_dict():
    uid = uuid.uuid4()
    current_date = datetime.now().today()

    invoice = Invoice.from_dict(
        {
            'uid': uid,
            'number': 'number-1',
            'invoiced_date': current_date,
            'order': 2,
            'customer': 3,
            'payment_term': 4,
        }
    )

    assert invoice.uid == uid
    assert invoice.number == 'number-1'
    assert invoice.invoiced_date == current_date
    assert invoice.order == 2
    assert invoice.customer == 3
    assert invoice.payment_term == 4
