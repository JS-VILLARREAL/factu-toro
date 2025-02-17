from rest_framework import serializers
from factu.models import Lot


class LotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lot
        fields = "__all__"


class LotPublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lot
        fields = ["id", "name_lot", "description"]
