from rest_framework import serializers
from .models import Kiosk
from product.serializers import ProductSerializer
from ifive_server.utils import get_resized_image_url
from ifive_server.utils import format_distance


class KioskSerializer(serializers.ModelSerializer):
    distance = serializers.FloatField(read_only=True, allow_null=True)
    formatted_distance = serializers.SerializerMethodField()
    products = ProductSerializer(many=True, read_only=True)
    resized_image_url = serializers.SerializerMethodField()

    def get_resized_image_url(self, obj):
        if obj.image:
            return get_resized_image_url(obj.image.name)
        return None

    class Meta:
        model = Kiosk
        fields = [
            "id",
            "name",
            "image",
            "resized_image_url",
            "address",
            "latitude",
            "longitude",
            "distance",
            "formatted_distance",
            "products",
        ]

    def get_formatted_distance(self, obj):
        return format_distance(obj.distance)


class KioskDetailSerializer(KioskSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Kiosk
        fields = [
            "id",
            "name",
            "image",
            "resized_image_url",
            "address",
            "latitude",
            "longitude",
            "distance",
            "formatted_distance",
            "products",
        ]
