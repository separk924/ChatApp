from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    username = models.CharField(max_length=20)
    password1 = models.CharField(max_length=20)
    password2 = models.CharField(max_length=20)