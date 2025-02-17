from rest_framework import viewsets, status
from ..serializers.auth import AuthSerializer
from django.contrib.auth.models import User
from drf_spectacular.utils import extend_schema


# @extend_schema(tags=["User"])
# class AuthViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = AuthSerializer
