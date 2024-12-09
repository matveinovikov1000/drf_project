from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets

from users.models import Payments
from users.serializers import PaymentsModelSerializer


class PaymentsModelViewSet(viewsets.ModelViewSet):
    queryset = Payments.objects.all()
    serializer_class = PaymentsModelSerializer

    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
    ]
    filterset_fields = (
        "paid_course",
        "payment_method",
    )
    ordering_fields = ("payment_date",)
