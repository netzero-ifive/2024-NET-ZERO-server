from rest_framework import serializers
from .models import Product, ALLERGEN_CHOICES
from ifive_server.utils import get_resized_image_url


class ProductSerializer(serializers.ModelSerializer):
    allergens = serializers.SerializerMethodField()
    resized_image_url = serializers.SerializerMethodField()

    def get_allergens(self, obj):
        allergen_dict = dict(ALLERGEN_CHOICES)
        return [
            allergen_dict.get(allergen.name, allergen.name)
            for allergen in obj.allergens.all()
        ]

    def get_resized_image_url(self, obj):
        if obj.image:
            return get_resized_image_url(obj.image.name)
        return None

    class Meta:
        model = Product
        fields = [
            "name",
            "price",
            "image",
            "resized_image_url",
            "size",
            "materials_ko",
            "nutrients_ko",
            "source_of_manufacture",
            "caution",
            "allergens",
        ]
