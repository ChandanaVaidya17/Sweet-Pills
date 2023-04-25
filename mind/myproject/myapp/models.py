from django.db import models


class user_details(models.Model):
    user_id = models.IntegerField()
    user_name = models.CharField(max_length=50)
    password = models.CharField(max_length=30)
    gender = models.CharField(max_length=6)
    dob = models.DateField()
    email = models.EmailField(max_length=250)
    class Meta:
        app_label="myapp"
    
    def __str__(self):
        return self.user_name

class personal(models.Model):
    user_id = models.IntegerField()
    family_history = models.CharField()
    #treatment = models.Charfield()
    leave = models.CharField()
    mental_health_consequence = models.CharField()
    physical_health_consequence = models.CharField()
    self_employed = models.CharField()

class work(models.Model):
    tech_company = models.CharField()
    work_interfere = models.CharField()
    no_employees = models.CharField()
    remote_work = models.CharField()
    benefits = models.CharField()
    care_options = models.CharField()
    wellness_program = models.CharField()
    seek_help = models.CharField()
    anonymity = models.CharField()
    coworkers = models.CharField()
    supervisor = models.CharField()
    mental_health_interview = models.CharField()
    phys_health_interview = models.CharField()
    mental_vs_physical = models.CharField()
    obs_consequence = models.CharField()


# Create your models here.
