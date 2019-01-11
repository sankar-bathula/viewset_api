from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet 
from viewsetapiapp.models import Employee
from viewsetapiapp.serializer import EmployeeSerializer

# Create your views here.
class EmployeeViewsetAPI(ModelViewSet):
	queryset = Employee.objects.all()
	serializer_class = EmployeeSerializer