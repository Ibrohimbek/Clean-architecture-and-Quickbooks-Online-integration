from core.use_cases import request_objects as ro


def test_build_invoice_list_request_object__without_parameters():
    req = ro.InvoiceListRequestObject()

    assert req.filters is None
    assert bool(req) is True


def test_build_invoice_list_request_object__from_empty_dict():
    req = ro.InvoiceListRequestObject.from_dict({})

    assert req.filters is None
    assert bool(req) is True


def test_build_invoice_list_request_object__with_empty_filters():
    req = ro.InvoiceListRequestObject(filters={})

    assert req.filters == {}
    assert bool(req) is True


def test_build_invoice_list_request_object__from_dict_with_empty_filters():
    req = ro.InvoiceListRequestObject.from_dict({'filters': {}})

    assert req.filters == {}
    assert bool(req) is True


def test_build_invoice_list_request_object__with_filters():
    req = ro.InvoiceListRequestObject(filters={'order': 1, 'number': 2})

    assert req.filters == {'order': 1, 'number': 2}
    assert bool(req) is True


def test_build_invoice_list_request_object__from_dict_with_filters():
    req = ro.InvoiceListRequestObject.from_dict({'filters': {'order': 1, 'number': 2}})

    assert req.filters == {'order': 1, 'number': 2}
    assert bool(req) is True


def test_build_invoice_list_request_object__from_dict_with_invalid_filters():
    req = ro.InvoiceListRequestObject.from_dict({'filters': 5})

    assert req.has_errors()
    assert req.errors[0]['parameter'] == 'filters'
    assert bool(req) is False
