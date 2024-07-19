from django.urls import path
from .views import BottleReturnListView

urlpatterns = [
    path("", BottleReturnListView.as_view(), name="bottle-return-list"),
    # path(
    #     "<int:pk>/",
    #     BottleReturnDetailView.as_view(),
    #     name="bottle-return-detail",
    # ),
]
