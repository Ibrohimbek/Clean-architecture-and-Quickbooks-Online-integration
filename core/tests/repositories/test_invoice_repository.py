import pytest

from core.repositories import invoice_repository
from core.shared.domain_model import DomainModel

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


def _check_results(domain_models_list, data_list):
    assert len(domain_models_list) == len(data_list)
    assert all([isinstance(dm, DomainModel) for dm in domain_models_list])
    assert set([dm.number for dm in domain_models_list]) == set([d['number'] for d in data_list])


def test_repository_list_without_parameters(invoices):
    repo = invoice_repository.InvoiceRepository(invoices)

    assert repo.list() == invoices


def test_repository_list_with_filters_unknown_key(invoices):
    repo = invoice_repository.InvoiceRepository(invoices)

    with pytest.raises(KeyError):
        repo.list(filters={'number_new': '111'})


def test_repository_list_with_filters_unknown_operator(invoices):
    repo = invoice_repository.InvoiceRepository(invoices)

    with pytest.raises(ValueError):
        repo.list(filters={'number__in': [20, 30]})


def test_repository_list_with_filters_price(invoices):
    repo = invoice_repository.InvoiceRepository(invoices)

    _check_results(repo.list(filters={'number': 111}), [invoice_3])
    _check_results(repo.list(filters={'number__eq': 111}), [invoice_3])
    _check_results(repo.list(filters={'number__lt': 111}), [invoice_1, invoice_2])
    _check_results(repo.list(filters={'number__gt': 111}), [invoice_4])
