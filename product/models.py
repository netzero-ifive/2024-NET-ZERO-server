from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Qrcode(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    data = models.CharField(max_length=100)
    image = models.ImageField(upload_to="qrcodes/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.qrcode
