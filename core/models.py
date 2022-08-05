from django.db import models
from sys import maxsize
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, UserManager, PermissionsMixin

class UserManager(BaseUserManager):

    def create_superuser(self, email, name, firstname, password, **other_fields):
        Useraccount = self.create_user(email=email, name=name, firstname=firstname,password=password, **other_fields)
        Useraccount.is_staff = True
        Useraccount.is_superuser = True
        Useraccount.save()
        return Useraccount

    def create_user(self, email, name, firstname, password, **other_fields):
        email = self.normalize_email(email)
        Useraccount = self.model(email=email, name=name,
                          firstname=firstname, **other_fields)
        Useraccount.set_password(password)
        Useraccount.save()
        return Useraccount


class UserAccount(AbstractBaseUser, PermissionsMixin):
    firstname = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, unique = True)
    password = models.TextField()
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    user_type = models.CharField(max_length=50, default="")
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS =  ['firstname', 'name']
        

class CompanyAccount(AbstractBaseUser):
    company_name = models.CharField(max_length=50)
    company_type = models.CharField(max_length=50)
    contact_firstname = models.CharField(max_length=50)
    contact_name = models.CharField(max_length=50)
    contact_email = models.EmailField(max_length=254, unique = True)
    password = models.TextField()
   



   

