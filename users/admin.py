from django.contrib import admin
from .models import Employee,User

admin.site.register(User)

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):

    list_display = ['id','employeeid', 'name', 'phone']
