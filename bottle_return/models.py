from django.db import models
import uuid, os
from django.utils.html import format_html
from ifive_server.settings import CLOUDFRONT_DOMAIN


def bottle_return_image_upload_to(instance, filename):
    ext = filename.split(".")[-1]
    filename = f"{uuid.uuid4()}.{ext}"
    return os.path.join("bottle_return", filename)


class BottleReturn(models.Model):
    name = models.CharField(default="페트병 반환소", max_length=100)
    image = models.ImageField(
        upload_to=bottle_return_image_upload_to, null=True, blank=True
    )

    address = models.CharField(max_length=100, blank=True)
    latitude = models.FloatField()
    longitude = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_resized_image_url(self):
        if self.image:
            base_name, _ = os.path.splitext(self.image.name)
            new_image_path = f"{base_name}.webp"
            return f"{CLOUDFRONT_DOMAIN}/{new_image_path}"
        return ""

    def display_resized_image(self):
        url = self.get_resized_image_url()
        if url:
            return format_html('<img src="{}" width="150" height="150" />', url)
        return "No Image"

    def __str__(self):
        return self.name + " " + self.address
