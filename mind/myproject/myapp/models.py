from django.db import models


class user_id(models.Model):
    user_name = models.CharField(max_length=50)
    password = models.CharField(max_length=30)
    gender = models.CharField(max_length=6)
    dob = models.DateField()
    email = models.EmailField(max_length=250)




# Create your models here.
