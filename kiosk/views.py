from rest_framework import generics
from .models import Kiosk
from .serializers import KioskSerializer


class KioskViews(generics.RetrieveAPIView):
    queryset = Kiosk.objects.all()
    serializer_class = KioskSerializer
