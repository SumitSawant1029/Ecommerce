from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class User1(User):
    username =User.username
    password = User.password
    first_name = User.first_name
    last_name = User.last_name
    email=User.email
    contact = models.IntegerField(max_length=10)
    birthdate = models.DateField()
    gender = models.CharField(max_length=15)

    def __str__(self):
        return self.username
