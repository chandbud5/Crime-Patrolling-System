from django.contrib import admin
from .models import Police_DB, Complaint
# Register your models here.

class complaint_view(admin.ModelAdmin):
    list_display = ['complainee', 'crime_title', 'latitude', 'longitude']
    search_fields = ['complainee']
    list_per_page = 20
    ordering = ['-id']

class police_view(admin.ModelAdmin):
    list_display = ['user', 'first_name', 'last_name', 'police_id', 'email_id', 'contact_number']
    search_fields = ['police_id', 'first_name', 'last_name']
    list_per_display = 20
    ordering = ['-id']

admin.site.register(Police_DB, police_view)
admin.site.register(Complaint, complaint_view)