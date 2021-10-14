from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class User_DB(models.Model):
    user = models.OneToOneField(User, on_delete = model.CASCADE)
    user_name = models.CharField(max_length = 256)
    aadhar_number = models.IntegerField()
    address = models.CharField(blank = True, max_length = 512)
    contact_number = models.IntegerField()
    joining_date = models.DateTimeField(auto_now_add=True)