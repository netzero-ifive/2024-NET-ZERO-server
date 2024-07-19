from rest_framework import serializers
from .models import Kiosk


class KioskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kiosk
        fields = "__all__"
