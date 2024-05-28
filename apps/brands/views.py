from django.shortcuts import render
from rest_framework import generics
from apps.brands.models import Brand
from apps.brands.serializers import BrandSerializer


class BrandListCreateView(generics.ListCreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
