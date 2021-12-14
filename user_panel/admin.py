from django.contrib import admin
from django.contrib import admin
from .models import User_DB
# Register your models here.

class User_DB_Admin(admin.ModelAdmin):
    list_display = ['user', 'first_name', 'last_name', 'aadhar_number', 'email_id']
    search_fields = ['first_name', 'last_name', 'aadhar_number', 'email_id', 'contact_number']
    list_per_page = 20
    ordering = ['-id']

admin.site.register(User_DB, User_DB_Admin)