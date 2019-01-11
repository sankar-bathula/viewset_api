from django.contrib import admin
from viewsetapiapp.models import Employee
from viewsetapiapp.serializer import EmployeeSerializer

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
	list_display = ['id', 'eno', 'ename', 'esal', 'eaddr']

admin.site.register(Employee, EmployeeAdmin)