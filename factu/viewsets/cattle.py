from rest_framework import viewsets
from factu.models import Cattle
from factu.serializers.cattle import CattleSerializer

from drf_spectacular.utils import extend_schema


@extend_schema(tags=["Cattle"])
class CattleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows cattle to be viewed or edited.
    """

    queryset = Cattle.objects.all().order_by("id")
    serializer_class = CattleSerializer
