from django.db import models
from django.contrib.auth.models import AbstractUser


# Class to override django user
class User(AbstractUser):
    pass
