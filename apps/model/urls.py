from django.urls import path
from apps.model import views as views


urlpatterns = [
    path("models/", views.ModelListCreateView.as_view(), name="model-list-create"),
    path("models/<int:pk>/", views.ModelRetrieveUpdateDestroyView.as_view(), name="model-detail-update-delete"),
]
