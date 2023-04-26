from django.contrib import admin
from .models import user_id, user_data, prediction, Admin

class usertable (admin.ModelAdmin):
    list_display = ("user_name","password","gender","dob","email")
    list_filter = ("gender","dob",)

admin.site.register(Admin)
admin.site.register(user_id,usertable)
admin.site.register(user_data)
admin.site.register(prediction)
# Register your models here.
