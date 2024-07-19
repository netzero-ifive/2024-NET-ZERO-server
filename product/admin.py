from django.contrib import admin

from .models import Product, Qrcode, Allergen

# admin.site.register(Product)
admin.site.register(Qrcode)
admin.site.register(Allergen)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "display_resized_image")
    readonly_fields = ("display_resized_image",)

    def display_resized_image(self, obj):
        return obj.display_resized_image()
