from rest_framework import generics
from apps.vessel.models import Vessel
from apps.vessel.serializers import VesselListSerializer, VesselSerializer


class ListCreateView(generics.ListCreateAPIView):
    queryset = Vessel.objects.all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return VesselListSerializer
        return VesselSerializer


class RetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Vessel.objects.all()
    serializer_class = VesselSerializer
