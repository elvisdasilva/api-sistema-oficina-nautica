from rest_framework import serializers
from apps.brands.models import Brand


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"

    def validate_description(self, value):
        if len(value) > 50:
            raise serializers.ValidationError(
                "Description must not be longer than 50 characters"
            )
