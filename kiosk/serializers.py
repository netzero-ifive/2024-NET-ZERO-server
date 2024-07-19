from rest_framework import serializers
from .models import Kiosk, Qrcode
from product.serializers import ProductSerializer


def format_distance(distance):
    if distance is None:
        return None
    if distance < 1000:
        return f"{int(distance)}m"
    else:
        return f"{distance/1000:.1f}km"


class KioskSerializer(serializers.ModelSerializer):
    distance = serializers.FloatField(read_only=True, allow_null=True)
    formatted_distance = serializers.SerializerMethodField()
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Kiosk
        fields = [
            "id",
            "name",
            "address",
            "latitude",
            "longitude",
            "created_at",
            "updated_at",
            "distance",
            "formatted_distance",
            "products",
        ]

    def get_formatted_distance(self, obj):
        return format_distance(obj.distance)


class KioskDetailSerializer(KioskSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta(KioskSerializer.Meta):
        fields = KioskSerializer.Meta.fields + ["products"]
