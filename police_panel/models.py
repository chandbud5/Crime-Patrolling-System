from django.db import models
from django.contrib.auth.models import User
from user_panel.models import User_DB
# Create your models here.
class Police_DB(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    first_name = models.CharField(blank = False, null = False, max_length = 256)
    last_name = models.CharField(max_length = 256)
    email_id = models.EmailField(blank=True, null=True)
    contact_number = models.IntegerField()
    police_id = models.CharField(max_length = 128)
    joining_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.police_name

class Complaint(models.Model):
    complainee = models.OneToOneField(User, on_delete=models.CASCADE)
    crime_title = models.CharField(max_length=200)
    threat = models.CharField(max_length=500)
    crime_description = models.TextField()
    latitude = models.FloatField(max_length=100)
    longitude = models.FloatField(max_length=100)
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.complainee) + " --> " + str(self.crime_title)
