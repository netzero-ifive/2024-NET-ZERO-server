from django.db import models
import uuid, os
from django.utils.html import format_html
from ifive_server.settings import CLOUDFRONT_DOMAIN


def kiosk_image_upload_to(instance, filename):
    ext = filename.split(".")[-1]
    filename = f"{uuid.uuid4()}.{ext}"
    return os.path.join("kiosk", filename)


class Kiosk(models.Model):
    name = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=100, blank=True)
    latitude = models.FloatField()
    longitude = models.FloatField()

    image = models.ImageField(upload_to=kiosk_image_upload_to, null=True, blank=True)

    products = models.ManyToManyField("product.Product", related_name="kiosks")

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
        return self.name


def qrcode_image_upload_to(instance, filename):
    ext = filename.split(".")[-1]
    filename = f"{uuid.uuid4()}.{ext}"
    return os.path.join("qrcodes", filename)


class Qrcode(models.Model):
    kiosk = models.ForeignKey(Kiosk, on_delete=models.CASCADE)
    data = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to=qrcode_image_upload_to, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
