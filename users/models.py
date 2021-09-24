from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager




class UserManager(BaseUserManager):
   
   def create_user(self, email, password, is_active=True):
      if not email:
         raise ValueError("User must have an email")
      if not password:
         raise ValueError("User must have a password")


      user = self.model(
         email=self.normalize_email(email)
      )

      user.set_password(password)  
      user.is_superuser = False
      user.is_staff = False
      user.active = is_active
      user.save(using=self._db)
      return user
      

   def create_superuser(self, email, password, **extra_fields):
      if not email:
         raise ValueError("User must have an email")
      if not password:
         raise ValueError("User must have a password")

      user = self.model(
         email=self.normalize_email(email)
      )
      user.set_password(password)
      user.is_superuser = True
      user.is_staff = True
      user.active = True
      user.save(using=self._db)
      return user



class User(AbstractUser):

   username = None
   email = models.CharField(max_length=200,unique=True)

   USERNAME_FIELD = 'email'
   REQUIRED_FIELDS = []

   objects = UserManager()

   class Meta:
      db_table="user"

