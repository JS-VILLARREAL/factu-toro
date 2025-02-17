from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from ..serializers.auth import AuthSerializer, AuthPublicSerializer
from drf_spectacular.utils import extend_schema


@api_view(["POST"])
def login_apiview(request):
    return Response({})


@extend_schema(
    request=AuthPublicSerializer, responses={201: AuthSerializer}, methods=["POST"]
)
class RegisterAPIView(APIView):
    def post(self, request):
        import pdb

        pdb.set_trace()
        # serializer = AuthPublicSerializer(data=request.data)
        # print(serializer)
        return Response({})
