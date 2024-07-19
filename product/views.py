from django.shortcuts import render

from rest_framework import views
from .models import ALLERGEN_CHOICES
from rest_framework.response import Response
from rest_framework import status


class AllergenListView(views.APIView):
    def get(self, request):
        allergens_korean = {
            "allergen_list": [allergen[1] for allergen in ALLERGEN_CHOICES]
        }
        return Response(allergens_korean, status=status.HTTP_200_OK)
