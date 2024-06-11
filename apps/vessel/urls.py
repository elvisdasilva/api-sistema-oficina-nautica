from django.urls import path
from apps.vessel import views as views


urlpatterns = [
    path("vessels/", views.ListCreateView.as_view(), name="vessel-list-create"),
    path("vessels/<int:pk>/", views.RetrieveUpdateView.as_view(), name="vessel-detail-update"),
]
