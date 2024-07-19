from django.urls import path
from .views import CreateProductView, ProductListView, generate_qr_code

urlpatterns = [
    path("products/", ProductListView.as_view(), name="product_list"),
    path("products/create", CreateProductView.as_view(), name="create_product"),
    path(
        "generate-qr-code/<int:product_id>/",
        generate_qr_code,
        name="generate_qr_code",
    ),
]
