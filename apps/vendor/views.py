from rest_framework import generics
from apps.vendor.models import Vendor
from apps.vendor.serializers import VendorSerializer


class ListCreateView(generics.ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer


class RetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
