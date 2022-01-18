from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class User_DB(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=256, default="")
    last_name = models.CharField(max_length=256, default="")
    email_id = models.EmailField(blank=True, null=True)
    contact_number = models.IntegerField()
    aadhar_number = models.IntegerField()
    address = models.CharField(null= True, max_length = 512)
    joining_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name + " " + self.last_name