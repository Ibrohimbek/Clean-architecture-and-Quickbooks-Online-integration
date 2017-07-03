import json

from core.repositories import invoice_repository
from core.serializers import invoice_serializer
from core.use_cases import invoice_use_case
from core.use_cases import request_objects as req
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


class InvoiceListAPIView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        data = request.query_params

        request_object = req.InvoiceListRequestObject.from_dict({})

        repo = invoice_repository.InvoiceRepository()
        use_case = invoice_use_case.InvoiceListUseCase(repo)

        response = use_case.execute(request_object)

        return Response(json.dumps(response.value, cls=invoice_serializer.InvoiceEncoder))
