from qb_online.core.use_cases import request_objects as ro


def test_build_invoice_list_request_object_without_parameters():
    req = ro.InvoiceListRequestObject()

    assert bool(req) is True


def test_build_invoice_list_request_object_from_empty_dict():
    req = ro.InvoiceListRequestObject.from_dict({})

    assert bool(req) is True
