from django.urls import path
from .views import KioskListView, KioskDetailView

urlpatterns = [
    path("", KioskListView.as_view(), name="kiosk-list"),
    path("<int:pk>/", KioskDetailView.as_view(), name="kiosk-detail"),
]
