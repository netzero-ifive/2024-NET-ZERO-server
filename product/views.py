from rest_framework import views, generics, status
from .models import ALLERGEN_CHOICES, Product
from rest_framework.response import Response
from .serializers import ProductSerializer


class AllergenListView(views.APIView):
    def get(self, request):
        allergens_korean = {
            "allergen_list": [allergen[1] for allergen in ALLERGEN_CHOICES]
        }
        return Response(allergens_korean, status=status.HTTP_200_OK)


class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "id"
