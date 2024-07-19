from rest_framework import generics
from .models import Kiosk
from .serializers import KioskSerializer, KioskDetailSerializer
from django.db.models import F, ExpressionWrapper, FloatField, Value
from django.db.models.functions import Sin, Cos, ACos, Radians


class KioskListView(generics.ListAPIView):
    serializer_class = KioskSerializer

    def get_queryset(self):
        queryset = Kiosk.objects.all()
        latitude = self.request.query_params.get("latitude")
        longitude = self.request.query_params.get("longitude")

        if latitude and longitude:
            try:
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
            except ValueError:
                queryset = queryset.annotate(
                    distance=Value(None, output_field=FloatField())
                )
        else:
            queryset = queryset.annotate(
                distance=Value(None, output_field=FloatField())
            )

        return queryset


class KioskDetailView(generics.RetrieveAPIView):
    queryset = Kiosk.objects.all()
    serializer_class = KioskDetailSerializer
