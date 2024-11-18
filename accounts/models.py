from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):

    phone_number = models.CharField(max_length=13)

    def __str__(self):
        return f'{self.phone_number}'
    


