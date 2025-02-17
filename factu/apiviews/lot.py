from rest_framework.views import APIView
from rest_framework.response import Response
from factu.models import Lot
from factu.serializers.lot import LotPublicSerializer


class LotAPIView(APIView):
    def get(self, request, *args, **kwargs):
        lot = Lot.objects.all()
        import pdb

        pdb.set_trace()
        serializer = LotPublicSerializer(lot, many=True)
        return Response(serializer.data)
