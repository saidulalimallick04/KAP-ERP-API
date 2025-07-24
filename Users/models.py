from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from django.contrib.auth.models import AbstractUser
from .manager import UserManager

# Create your models here.


class User(AbstractUser):
    
    date_joined = None
    
    username = models.CharField(_("Username"),max_length=30,unique=True)
    
    first_name = models.CharField(_("first name"), max_length=50)
    middle_name = models.CharField(_("Middle Name"), max_length=50,blank=True)
    last_name = models.CharField(_("last name"), max_length=50,blank=True)
    
    phone_number = models.CharField(max_length=10,unique=True)
    secondary_phone = models.CharField(max_length=10,blank=True)
    whatsapp_number = models.CharField(max_length=10,blank=True)
    
    user_type = models.CharField(_("User Type"),max_length=25)
    created_at = models.DateTimeField(_("Account Created Date"), default=timezone.now)
    
    USERNAME_FIELD = ("phone_number")
    REQUIRED_FIELDS = []
    
    objects = UserManager()
    def __str__(self) -> str:
        return f"{self.username} ||| {self.phone_number}"