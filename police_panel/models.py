from django.db import models
from django.contrib.auth.models import User

# Create your models here.
def Police_DB(models.Model):
    user = models.OneToOneField(User, on_delete = model.CASCADE)
    police_name = models.CharField(blank = False, null = False, max_length = 256)
    contact_number = models.IntegerField()
    police_id = models.CharField(max_length = 128)
    joining_date = models.DateTimeField(auto_now_add=True)
