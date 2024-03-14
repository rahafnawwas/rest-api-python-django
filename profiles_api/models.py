from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfilesManger(BaseUserManager):
    """manager for user class"""
    def create_user(self,email,name,password=None):
        """create a new user profile"""
        if not email:
            raise valueError('user must have an email')

        email=self.normalize_email(email)
        user =self.model(email=email,name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user


    def create_superuser(self,email,name,password):
        self.create_user(email,name,password)
        user.is_superuser=True
        user.is_staff=True
        user.save(using=self._db)

        return user

# Create your models here.
class UserProfiles(AbstractBaseUser,PermissionsMixin):
    """database user models in system"""
    email= models.EmailField(max_length=255,unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = UserProfilesManger()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """retrieve full name of user"""
        return self.name
    def get_short_name(self):
        return self.name

    def __str__(self):
        return self.email
