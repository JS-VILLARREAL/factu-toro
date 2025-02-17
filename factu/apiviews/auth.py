from rest_framework.response import Response
from ..serializers.auth import AuthPublicSerializer
from django.contrib.auth.models import User
from drf_spectacular.utils import extend_schema
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.views import APIView
from django.db import transaction


class LoginAPIView(APIView):
    pass


class SignupAPIView(APIView):
    serializer_class = AuthPublicSerializer

    @extend_schema(
        request=AuthPublicSerializer,
        responses={201: AuthPublicSerializer},
        methods=["POST"],
    )
    def post(self, request):
        serializer = self.get_serializer(data=request.data)

        import pdb

        pdb.set_trace()
        if serializer.is_valid():
            with transaction.atomic():
                serializer.save()
                user = serializer.instance
                user.set_password(request.data["password"])
                user.save()
                token = Token.objects.create(user=user)
                return Response(
                    {"token": token.key, "user": serializer.data},
                    status=status.HTTP_201_CREATED,
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
