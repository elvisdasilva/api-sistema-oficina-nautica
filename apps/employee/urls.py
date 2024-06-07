from django.urls import path
from apps.employee import views as views

urlpatterns = [
    path("employees/", views.EmployeeListCreateView.as_view(), name="employee-list-create"),
    path("employees/<int:pk>/", views.EmployeeRetrieveUpdateDestroyView.as_view(), name="employee-detail-update-delete"),
]
