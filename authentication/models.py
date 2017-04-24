from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core import validators
from datetime import timezone

class UserManager(models.Manager):
    pass

# Class to override django user
class User(AbstractUser):
    email = models.EmailField(
        _('Email Address'), unique=True,
        error_messages={
            'unique': _("A user with that email already exists."),
        }
    )
    username = models.CharField(
        _('Username'), max_length=30, unique=True, blank=True, null=True,
        help_text=_('30 characters or fewer. Letters, digits and _ only.'),
        validators=[
            validators.RegexValidator(
                r'^\w+$',
                _('Enter a valid username. This value may contain only '
                  'letters, numbers and _ character.'),
                'invalid'
            ),
        ],
        error_messages={
            'unique': _("The username is already taken."),
        }
    )
    is_staff = models.BooleanField(
        _('Staff Status'), default=False,
        help_text=_('Designates whether the user can log into this admin '
                    'site.')
    )
    is_active = models.BooleanField(
        _('Active'), default=True,
        help_text=_('Designates whether this user should be treated as '
                    'active. Unselect this instead of deleting accounts.')
    )
    date_joined = models.DateTimeField(_('Date Joined'), default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    class Meta(object):
        verbose_name = _('User')
        verbose_name_plural = _('Users')
        abstract = False
