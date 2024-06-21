from django.urls import path
from apps.vendor import views as views

urlpatterns = [
    path("vendors/", views.ListCreateView.as_view(), name="vendor-list-create"),
    path("vendors/<int:pk>/", views.RetrieveUpdateView.as_view(), name="vendor-detail-update")
]
