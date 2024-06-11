from rest_framework import serializers
from apps.vessel.models import Vessel


class VesselSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vessel
        fields = "__all__"
