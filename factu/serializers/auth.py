from django.contrib.auth.models import User
from rest_framework import serializers


class AuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class AuthPublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "email", "password"]
