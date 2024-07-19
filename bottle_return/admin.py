from django.contrib import admin
from .models import BottleReturn


@admin.register(BottleReturn)
class BottleReturnAdmin(admin.ModelAdmin):
    list_display = ("name", "display_resized_image")
    readonly_fields = ("display_resized_image",)
