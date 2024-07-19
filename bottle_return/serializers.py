from rest_framework import serializers
from .models import BottleReturn
from ifive_server.utils import get_resized_image_url, format_distance


class BottleReturnSerializer(serializers.ModelSerializer):
    distance = serializers.FloatField(read_only=True)
    formatted_distance = serializers.SerializerMethodField()
    resized_image_url = serializers.SerializerMethodField()

    def get_resized_image_url(self, obj):
        if obj.image:
            return get_resized_image_url(obj.image.name)
        return None

    class Meta:
        model = BottleReturn
        fields = [
            "id",
            "address",
            "image",
            "resized_image_url",
            "latitude",
            "longitude",
            "distance",
            "formatted_distance",
        ]

    def get_formatted_distance(self, obj):
        return format_distance(obj.distance)
