from django.contrib import admin

from .models import Product, Qrcode, Allergen

admin.site.register(Product)
admin.site.register(Qrcode)
admin.site.register(Allergen)
