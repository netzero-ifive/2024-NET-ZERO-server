from rest_framework import generics
from .models import BottleReturn
from .serializers import BottleReturnSerializer


class KioskViews(generics.ListAPIView):
    queryset = BottleReturn.objects.all()
    serializer_class = BottleReturnSerializer
