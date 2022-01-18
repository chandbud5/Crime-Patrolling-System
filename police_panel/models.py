from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Police_DB(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(blank = False, null = False, max_length = 256)
    last_name = models.CharField(max_length = 256)
    email_id = models.EmailField(blank=True, null=True)
    contact_number = models.IntegerField()
    police_id = models.CharField(max_length = 128)
    joining_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name

class Complaint(models.Model):
    complainee = models.ForeignKey(User, on_delete=models.CASCADE)
    crime_title = models.CharField(max_length=200)
    threat = models.CharField(max_length=500)
    crime_description = models.TextField()
    latitude = models.FloatField(max_length=100)
    longitude = models.FloatField(max_length=100)
    status = models.CharField(max_length=50, default="Registered")
    police_assigned = models.ForeignKey(Police_DB, on_delete=models.SET_NULL, null=True)
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.complainee) + " --> " + str(self.crime_title)

class Reports(models.Model):
    complaint = models.OneToOneField(Complaint, on_delete=models.RESTRICT)
    report_description = models.TextField()
    officer_incharge = models.ForeignKey(Police_DB, on_delete=models.DO_NOTHING)
    comments = models.CharField(max_length=128, null=True, blank=True)
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.complaint)