from django.contrib import admin
from .models import Kiosk


@admin.register(Kiosk)
class KioskAdmin(admin.ModelAdmin):
    list_display = ("name", "display_resized_image")
    readonly_fields = ("display_resized_image",)
