from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import MyUserManager

class MyUser(AbstractBaseUser):
    country_code = models.CharField(max_length=4)
    phone_number = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=55, default='User', null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['country_code', 'phone_number']

    def __str__(self):
        return self.email

    def full_phone_number(self):
        return f"{self.country_code}{self.phone_number}"

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
