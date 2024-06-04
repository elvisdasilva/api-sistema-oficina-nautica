from django.urls import path
from . import views as views


urlpatterns = [
    path("customer/", views.CustomerListCreateView.as_view(), name="customer-list-create"),
    path("customer/<int:pk>/", views.CustomerRetrieveUpdateDestroyView.as_view(), name="customer-detail-update-delete"),
]
