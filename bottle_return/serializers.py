from rest_framework import serializers
from .models import BottleReturn


def format_distance(distance):
    if distance is None:
        return None
    if distance < 1000:
        return f"{int(distance)}m"
    else:
        return f"{distance/1000:.1f}km"


class BottleReturnSerializer(serializers.ModelSerializer):
    distance = serializers.FloatField(read_only=True)
    formatted_distance = serializers.SerializerMethodField()

    class Meta:
        model = BottleReturn
        fields = [
            "id",
            "address",
            "image",
            "latitude",
            "longitude",
            "distance",
            "formatted_distance",
        ]

    def get_formatted_distance(self, obj):
        return format_distance(obj.distance)
