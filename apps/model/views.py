from rest_framework import generics
from apps.model.models import Model
from apps.model.serializers import ModelSerializer


class ModelListCreateView(generics.ListCreateAPIView):
    queryset = Model.objects.all()
    serializer_class = ModelSerializer


class ModelRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Model.objects.all()
    serializer_class = ModelSerializer
