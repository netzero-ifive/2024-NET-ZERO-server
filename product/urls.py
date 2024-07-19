from django.urls import path, include
from . import views


urlpatterns = [
    path("allergens_list/", views.AllergenListView.as_view(), name="allergen_list"),
]
