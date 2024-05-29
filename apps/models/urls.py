from django.urls import path
from apps.models import views as views


urlpatterns = [
    path("models/", views.ModelListCreateView.as_view(), name="model-detail-view"),
]
