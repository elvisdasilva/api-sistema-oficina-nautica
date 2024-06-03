from django.urls import path
from . import views as views

urlpatterns = [
    path("brands/", views.BrandListCreateView.as_view(), name="brand-list-create"),
    path("brands/<int:pk>/", views.BrandRetrieveUpdateDestroyView.as_view(), name="brand-detail-view")
]
