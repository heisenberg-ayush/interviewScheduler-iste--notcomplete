from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager
from django.core.validators import MaxValueValidator


class CustomUser(AbstractBaseUser, PermissionsMixin):
    full_name = models.CharField(_('full name'), max_length=170, default=None)
    email = models.EmailField(_('email address'), unique=True)
    reg_num = models.PositiveIntegerField(_('registration number'), unique=True,  validators=[MaxValueValidator(999999999)], default=None)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name', 'reg_num']

    objects = CustomUserManager()

    def __str__(self):
        return self.full_name