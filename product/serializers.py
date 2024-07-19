from rest_framework import serializers
from .models import Product, ALLERGEN_CHOICES


class ProductSerializer(serializers.ModelSerializer):
    allergens = serializers.SerializerMethodField()

    def get_allergens(self, obj):
        allergen_dict = dict(ALLERGEN_CHOICES)
        return [
            allergen_dict.get(allergen.name, allergen.name)
            for allergen in obj.allergens.all()
        ]

    class Meta:
        model = Product
        fields = [
            "name",
            "price",
            "description",
            "materials_ko",
            "nutrients_ko",
            "allergens",
        ]
