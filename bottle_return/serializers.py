from rest_framework import serializers
from .models import BottleReturn


class KioskSerializer(serializers.ModelSerializer):
    class Meta:
        model = BottleReturn
        fields = "__all__"
