from django.db import models
import uuid, os


class Kiosk(models.Model):
    address = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()

    products = models.ManyToManyField("product.Product", related_name="kiosks")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

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
