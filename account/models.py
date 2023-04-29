from django.db import models

# Create your models here.

from django.db import models

from django.contrib.auth.models import AbstractUser
from .manager import UserManager


class MyUser(AbstractUser):
    REQUIRED_FIELDS = ["first_name", "last_name"]
    USERNAME_FIELD = "email"
    username = models.CharField(("username"), max_length=30, blank=True)
    email = models.EmailField("Email", blank=False, null=False, unique=True)
    first_name = models.CharField(("first name"), max_length=150, blank=False)
    last_name = models.CharField(("last name"), max_length=150, blank=False)
    reward_point = models.IntegerField(default=0)
    password = models.CharField(("Password"), max_length=150)
    confirm_password = models.CharField(("Confirm Password"), max_length=150, null=True)

    joining_date = models.DateTimeField(auto_now=True)

    # def self__str__(self):
    #     return self.first_name

    objects = UserManager()
    groups = None
    user_permissions = None



class otp(models.Model):
    otp = models.CharField(max_length=6)
    email = models.EmailField()

    def __str__(self):
        return f"{self.otp} for {self.email}"
