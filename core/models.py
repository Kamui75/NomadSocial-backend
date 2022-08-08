from contextlib import nullcontext
from django.db import models
from sys import maxsize
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, UserManager, PermissionsMixin, AbstractUser
from django.utils.translation import ugettext_lazy as _

class UserManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)


class UserAccount(AbstractUser, PermissionsMixin):
    username = None
    email = models.EmailField(max_length=254, unique = True)
    company_name = models.TextField(default="")
    password2 = models.TextField(default="")
    user_type = models.CharField(max_length=50, default="")
    is_company = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS =  ['first_name', 'last_name']

    objects = UserManager()

    def __str__(self):
        return self.email
        

   



   

