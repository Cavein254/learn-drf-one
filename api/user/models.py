from django.db import models
from django.contrib.auth import models as auth_models

class UserManager(auth_models.BaseUserManager):
    def create_user(self, first_name, last_name, email, password, is_staff=False, is_superuser=False) -> 'user':
        if not email:
            raise ValueError("User must have an email")
        if not first_name:
            raise ValueError("User must have an First Name")
        if not last_name:
            raise ValueError("User must have an Last Name")
        
        user = self.model(email=self.normalize_email(email))
        user.first_name = first_name
        user.last_name = last_name
        user.set_password(password)
        user.is_active = True
        user.is_staff = is_staff
        user.is_superuser = is_superuser
        user.save()

        return user
    
    def create_superuser(self, first_name, last_name, password, email) -> 'user':
        user = self.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
            is_staff=True
            is_superuser=True
        )
        user.save()

        return user


    

class User(auth_models.AbstractUser):
    first_name = models.CharField(verbose_name="First Name", max_length=100)
    last_name = models.CharField(verbose_name="Last Name", max_length=100)
    email = models.CharField(verbose_name="email", max_length=255)
    password = models.CharField(verbose_name="password", max_length=255)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']