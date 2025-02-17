from rest_framework import viewsets
from factu.models import Lot
from factu.serializers.lot import LotSerializer

from drf_spectacular.utils import extend_schema


@extend_schema(tags=["Lot"])
class LotViewSet(viewsets.ModelViewSet):
    queryset = Lot.objects.all()
    serializer_class = LotSerializer

    # @extend_schema(responses={201: LotSerializer()})
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
