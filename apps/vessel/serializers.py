from rest_framework import serializers
from apps.vessel.models import Vessel


class VesselListSerializer(serializers.ModelSerializer):
    brand = serializers.ReadOnlyField(source="brand.description")
    model = serializers.ReadOnlyField(source="model.description")
    customer = serializers.ReadOnlyField(source="customer.full_name")

    class Meta:
        model = Vessel
        fields = "__all__"


class VesselSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vessel
        fields = "__all__"
