from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core import validators
from django.utils import timezone

class UserManager(models.Manager):
    pass

# Class to override django user
class User(AbstractUser):
    email = models.EmailField(
        ('Email Address'), unique=True,
        error_messages={
            'unique': ("A user with that email already exists."),
        }
    )
    username = models.CharField(
        ('Username'), max_length=30, unique=True, blank=True, null=True,
        help_text=('30 characters or fewer. Letters, digits and _ only.'),
        validators=[
            validators.RegexValidator(
                r'^\w+$',
                ('Enter a valid username. This value may contain only letters, numbers and _ character.'),
                'invalid'
            ),
        ],
        error_messages={
            'unique': ("The username is already taken."),
        }
    )
    is_staff = models.BooleanField(
        ('Staff Status'), default=False,
        help_text=('Designates whether the user can log into this admin site.')
    )
    is_active = models.BooleanField(
        ('Active'),
        default=True,
        help_text=('Designates whether this user should be treated as active. Unselect this instead of deleting accounts.')
    )
    date_joined = models.DateTimeField(('Date Joined'), default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    class Meta(object):
        verbose_name = ('User')
        verbose_name_plural = ('Users')
        abstract = False
