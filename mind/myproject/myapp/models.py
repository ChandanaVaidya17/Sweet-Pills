from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class user_id(models.Model):
    user_name = models.CharField(max_length=50)
    password = models.CharField(max_length=30)
    gender = models.CharField(max_length=6)
    dob = models.DateField()
    email = models.EmailField(max_length=250)

    def save(self, *args, **kwargs):
        self.password = make_password(self.password) # Hash password before saving
        super().save(*args, **kwargs)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)
    
    class Meta:
        app_label="myapp"
    
    def __str__(self):
        return self.user_name
    
class user_data(models.Model):
    user_id = models.OneToOneField('myapp.user_id', on_delete=models.CASCADE, primary_key=True)
    self_employed = models.CharField(choices=(("yes", "Yes"), ("no", "No")), max_length=10)
    family_history = models.CharField(choices=(("yes", "Yes"), ("no", "No")), max_length=10)
    treatment_before = models.CharField(choices=(("yes", "Yes"), ("no", "No")), max_length=10)
    mental_interfere = models.CharField(choices=(("often", "Often"), ("sometimes", "Sometimes"), ("rarely", "Rarely"), ("never", "Never"), ("don't know", "Don't know")), max_length=20)
    num_employees = models.CharField(choices=(("1-5", "1-5"), ("6-25", "6-25"), ("26-100", "26-100"), ("100-500", "100-500"), ("500-1000", "500-1000"), ("1000<", "1000<")), max_length=10)
    work_remotely = models.CharField(choices=(("yes", "Yes"), ("no", "No")), max_length=10)
    tech_company = models.CharField(choices=(("yes", "Yes"), ("no", "No")), max_length=10)
    mental_health_benefits = models.CharField(choices=(("yes", "Yes"), ("no", "No"), ("don't know", "Don't know")), max_length=20)
    mental_health_options = models.CharField(choices=(("yes", "Yes"), ("no", "No"), ("not sure", "Not sure")), max_length=20)
    mental_health_wellness_program = models.CharField(choices=(("yes", "Yes"), ("no", "No"), ("don't know", "Don't know")), max_length=20)
    mental_health_resources = models.CharField(choices=(("yes", "Yes"), ("no", "No"), ("don't know", "Don't know")), max_length=20)
    anonymity_protected = models.CharField(choices=(("yes", "Yes"), ("no", "No"), ("don't know", "Don't know")), max_length=20)
    medical_leave = models.CharField(choices=(("very easy", "Very easy"), ("somewhat easy", "Somewhat easy"), ("somewhat difficult", "Somewhat difficult"), ("very difficult", "Very difficult"), ("don't know", "Don't know")), max_length=20)
    discuss_mental_health_consequences = models.CharField(choices=(("yes", "Yes"), ("no", "No"), ("maybe", "Maybe")), max_length=10)
    discuss_physical_health_consequences = models.CharField(choices=(("yes", "Yes"), ("no", "No"), ("maybe", "Maybe")), max_length=10)
    discuss_mental_health_coworkers = models.CharField(choices=(("yes", "Yes"), ("no", "No"), ("some of them", "Some of them")), max_length=20)
    discuss_mental_health_supervisor = models.CharField(choices=(("yes", "Yes"), ("no", "No"), ("some of them", "Some of them")), max_length=20)
    bring_up_mental_health_interview = models.CharField(choices=(("yes", "Yes"), ("no", "No"), ("maybe", "Maybe")), max_length=10)
    bring_up_hysical_health_interview = models.CharField(choices=(("yes", "Yes"), ("no", "No"), ("maybe", "Maybe")), max_length=10)
    employer_take_serious = models.CharField(choices=(("yes", "Yes"), ("no", "No"), ("don't know", "Don't Know")), max_length=10)
    negative_consequences_coworkers = models.CharField(choices=(("yes", "Yes"), ("no", "No")), max_length=10)

class prediction(models.Model):
    user_id = models.OneToOneField('myapp.user_id', on_delete=models.CASCADE, primary_key=True)
    treatment = models.CharField(max_length=1000)

class Admin(models.Model):
    user_name = models.CharField(max_length=25)
    password = models.CharField(max_length=50)



# Create your models here.
