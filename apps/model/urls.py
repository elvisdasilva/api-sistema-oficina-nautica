from django.urls import path
from apps.model import views as views


urlpatterns = [
    path("models/", views.ModelListCreateView.as_view(), name="model-detail-view"),
]
