from django.db import models


class user_id(models.Model):
    user_name = models.CharField(max_length=50)
    password = models.CharField(max_length=30)
    gender = models.CharField(max_length=6)
    dob = models.DateField()
    email = models.EmailField(max_length=250)
    class Meta:
        app_label="myapp"
    
    def __str__(self):
        return self.user_name




# Create your models here.
