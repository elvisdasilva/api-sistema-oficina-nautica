from rest_framework import serializers
from apps.models.models import Model


class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Model
        fields = "__all__"

    def validate_description(self, value):
        if len(value) > 50:
            raise serializers.ValidationError(
                "Description must not be longer than 50 characters"
            )
