from django.contrib import admin

# Register your models here.
from .models import MyUser

@admin.register(MyUser)

class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','email','password','joining_date','confirm_password')