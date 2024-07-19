from django.db import models
import uuid, os


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(null=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


def qrcode_image_upload_to(instance, filename):
    ext = filename.split(".")[-1]
    filename = f"{uuid.uuid4()}.{ext}"
    return os.path.join("qrcodes", filename)


ALLERGEN_CHOICES = [
    ("POULTRY", "난류"),
    ("MILK", "우유"),
    ("BUCKWHEAT", "메밀"),
    ("PEANUT", "땅콩"),
    ("SOYBEAN", "대두"),
    ("WHEAT", "밀"),
    ("MACKEREL", "고등어"),
    ("CRAB", "게"),
    ("SHRIMP", "새우"),
    ("PORK", "돼지고기"),
    ("PEACH", "복숭아"),
    ("TOMATO", "토마토"),
    ("SULFITE", "아황산류"),
    ("WALNUT", "호두"),
    ("CHICKEN", "닭고기"),
    ("BEEF", "쇠고기"),
    ("SQUID", "오징어"),
    ("SHELLFISH", "조개류"),
]


class Allergen(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, choices=ALLERGEN_CHOICES)

    def __str__(self):
        return self.name


class Qrcode(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    data = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to=qrcode_image_upload_to, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
