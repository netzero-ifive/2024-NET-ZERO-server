from django.db import models
import uuid, os


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(null=True, blank=True)
    description = models.TextField(blank=True)
    size = models.CharField(max_length=100, blank=True)  # 총 내용량

    def get_nutrients_ko_default():
        return {
            "serving_size": "100ml",
            "calories": "30kcal",
            "detail": {
                "탄수화물": {
                    "amount": "0g",
                    "percent": "0%",
                },
                "당류": {
                    "amount": "0g",
                    "percent": "0%",
                },
                "단백질": {
                    "amount": "0g",
                    "percent": "0%",
                },
                "지방": {
                    "amount": "0g",
                    "percent": "0%",
                },
                "포화지방": {
                    "amount": "0g",
                    "percent": "0%",
                },
                "트랜스지방": {
                    "amount": "0g",
                    "percent": "0%",
                },
                "콜레스트롤": {
                    "amount": "0mg",
                    "percent": "0%",
                },
                "나트륨": {
                    "amount": "0mg",
                    "percent": "0%",
                },
            },
        }

    materials_ko = models.TextField(blank=True, default="")  # 원재료
    nutrients_ko = models.JSONField(
        blank=True, default=get_nutrients_ko_default()
    )  # 영양정보
    source_of_manufacture = models.TextField(blank=True, default="")  # 제조원
    caution = models.TextField(blank=True, default="")  # 주의사항

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id) + ": " + self.name


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
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="allergens"
    )
    name = models.CharField(max_length=100, choices=ALLERGEN_CHOICES)

    def __str__(self):
        return self.name


class Qrcode(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    data = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to=qrcode_image_upload_to, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
