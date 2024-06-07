from django.urls import path
from apps.customer import views as views


urlpatterns = [
    path("customer/", views.CustomerListCreateView.as_view(), name="customer-list-create"),
    path("customer/<int:pk>/", views.CustomerRetrieveUpdateView.as_view(), name="customer-detail-update"),
]
