from unittest import mock

import pytest

from qb_online.core.domain.invoice import Invoice
from qb_online.core.shared import response_object as res
from qb_online.core.use_cases import invoice_use_case as uc, request_objects as req


invoice_1 = {
    'uid': 'f853578c-fc0f-4e65-81b8-566c5dffa35a',
    'number': 1, 'invoiced_date': '2017-05-20',
    'order': 2, 'customer': 3, 'payment_term': 4
}

invoice_2 = {
    'uid': 'fe2c3195-aeff-487a-a08f-e0bdc0ec6e9a',
    'number': 11, 'invoiced_date': '2017-05-20',
    'order': 22, 'customer': 33, 'payment_term': 44
}

invoice_3 = {
    'uid': '913694c6-435a-4366-ba0d-da5334a611b2',
    'number': 111, 'invoiced_date': '2017-05-20',
    'order': 222, 'customer': 333, 'payment_term': 444
}

invoice_4 = {
    'uid': 'eed76e77-55c1-41ce-985d-ca49bf6c0585',
    'number': 1111, 'invoiced_date': '2017-05-20',
    'order': 2222, 'customer': 3333, 'payment_term': 4444
}


@pytest.fixture
def invoices():
    return [invoice_1, invoice_2, invoice_3, invoice_4]


def test_invoice_list_without_parameters(invoices):
    repo = mock.Mock()
    repo.list.return_value = invoices

    invoice_list_use_case = uc.InvoiceListUseCase(repo)
    request_object = req.InvoiceListRequestObject.from_dict({})

    response_object = invoice_list_use_case.execute(request_object)

    assert bool(response_object) is True
    repo.list.assert_called_with(filters=None)

    assert response_object.value == invoices


def test_invoice_list_with_filters(invoices):
    repo = mock.Mock()
    repo.list.return_value = invoices

    storageroom_list_use_case = uc.InvoiceListUseCase(repo)

    qry_filters = {'load': 5}
    request_object = req.InvoiceListRequestObject.from_dict({'filters': qry_filters})

    response_object = storageroom_list_use_case.execute(request_object)

    assert bool(response_object) is True
    repo.list.assert_called_with(filters=qry_filters)
    assert response_object.value == invoices


def test_invoice_list_handles_generic_error():
    repo = mock.Mock()
    repo.list.side_effect = Exception('Just an error message')

    invoice_list_use_case = uc.InvoiceListUseCase(repo)
    request_object = req.InvoiceListRequestObject.from_dict({})

    response_object = invoice_list_use_case.execute(request_object)

    assert bool(response_object) is False
    assert response_object.value == {
        'type': res.ResponseFailure.SYSTEM_ERROR,
        'message': "Exception: Just an error message"
    }


def test_invoice_list_handles_bad_request():
    repo = mock.Mock()

    invoice_list_use_case = uc.InvoiceListUseCase(repo)
    request_object = req.InvoiceListRequestObject.from_dict({'filters': 5})

    response_object = invoice_list_use_case.execute(request_object)

    assert bool(response_object) is False
    assert response_object.value == {
        'type': res.ResponseFailure.PARAMETERS_ERROR,
        'mess
    }
