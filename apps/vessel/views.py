from rest_framework import generics
from apps.vessel.models import Vessel
from apps.vessel.serializers import VesselSerializer


class ListCreateView(generics.ListCreateAPIView):
    queryset = Vessel.objects.all()
    serializer_class = VesselSerializer


class RetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Vessel.objects.all()
    serializer_class = VesselSerializer
