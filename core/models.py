from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager


# Create your models here.
class MyManager(BaseUserManager):
    def create_user(self,username,password,email,**extrafields):
        if not (username and email):
            raise ValueError("USername Required")
    
        user=self.model(username=username,email=self.normalize_email(email),**extrafields)
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self,username,password,email,**extrafields):
        extrafields.setdefault("is_staff",True)
        extrafields.setdefault("is_superuser",True)
        return self.create_user(username,password,email,**extrafields)

    
class CustomUser(AbstractBaseUser,PermissionsMixin):
    username=models.CharField(max_length=50,unique=True,blank=False)
    phone_number=models.IntegerField(blank=False)
    fullname=models.CharField(max_length=50,blank=False)
    email=models.EmailField(max_length=254,blank=False)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    REQUIRED_FIELDS=["phone_number","fullname","email"]
    USERNAME_FIELD="username"
    objects=MyManager()
    
    def __str__(self):
        return self.username
