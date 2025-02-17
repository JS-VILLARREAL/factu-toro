from rest_framework import serializers
from factu.models import Cattle


class CattleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cattle
        fields = "__all__"
