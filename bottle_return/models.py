from django.db import models
import uuid, os


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

    def __str__(self):
        return self.name + " " + self.address
