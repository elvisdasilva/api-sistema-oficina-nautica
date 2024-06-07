from rest_framework import generics
from apps.employee.models import Employee
from apps.employee.serializers import EmployeeSerializer


class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset = Employee
    serializer_class = EmployeeSerializer


class EmployeeRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Employee
    serializer_class = EmployeeSerializer
