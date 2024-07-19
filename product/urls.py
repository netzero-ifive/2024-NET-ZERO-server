from django.urls import path, include
from . import views


urlpatterns = [
    path(
        "api/product/<int:id>/",
        views.ProductDetailView.as_view(),
        name="product_detail",
    ),
    path("api/allergens_list/", views.AllergenListView.as_view(), name="allergen_list"),
]
