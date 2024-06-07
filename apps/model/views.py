from rest_framework import generics
from apps.model.models import Model
from apps.model.serializers import ModelSerializer


class ModelListCreateView(generics.ListCreateAPIView):
    queryset = Model.objects.all()
    serializer_class = ModelSerializer


class ModelRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Model.objects.all()
    serializer_class = ModelSerializer
