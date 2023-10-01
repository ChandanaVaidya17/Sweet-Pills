from django.contrib import admin
from .models import user_id

class usertable (admin.ModelAdmin):
    list_display = ("user_name","password","gender","dob","email")
    list_filter = ("gender","dob",)

admin.site.register(user_id,usertable)
# Register your models here.
