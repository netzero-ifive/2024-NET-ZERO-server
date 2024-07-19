from rest_framework import generics
from .models import BottleReturn
from .serializers import BottleReturnSerializer
from django.db.models import F, ExpressionWrapper, FloatField
from django.db.models.functions import Sin, Cos, ACos, Radians


def format_distance(distance):
    if distance is None:
        return None
    if distance < 1000:
        return f"{int(distance)}m"
    else:
        return f"{distance/1000:.1f}km"


class BottleReturnListView(generics.ListAPIView):
    serializer_class = BottleReturnSerializer

    def get_queryset(self):
        queryset = BottleReturn.objects.all()
        latitude = self.request.query_params.get("latitude")
        longitude = self.request.query_params.get("longitude")

        if latitude and longitude:
            latitude = float(latitude)
            longitude = float(longitude)

            # Haversine formula
            queryset = queryset.annotate(
                distance=ExpressionWrapper(
                    6371
                    * ACos(
                        Cos(Radians(latitude))
                        * Cos(Radians(F("latitude")))
                        * Cos(Radians(F("longitude")) - Radians(longitude))
                        + Sin(Radians(latitude)) * Sin(Radians(F("latitude")))
                    )
                    * 1000,  # Convert km to meters
                    output_field=FloatField(),
                )
            ).order_by("distance")

        return queryset


class BottleReturnDetailView(generics.RetrieveAPIView):
    queryset = BottleReturn.objects.all()
    serializer_class = BottleReturnSerializer
