from django.db import models

# from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User

# from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.utils.http import urlquote
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import BaseUserManager

# Create your models here.
import datetime

"""
Provides year choices for year_started_learning
"""
year_choices = []
for r in range(1980, (datetime.datetime.now().year + 1)):
    year_choices.append((r, r))


class ProfileManager(BaseUserManager):
    def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
        """
        Creates and saves User
        """
        now = timezone.now()
        if not email:
            raise ValueError("The given email must be set")
        email = email
        user = self.model(
            email=email,
            is_staff=is_staff,
            is_active=True,
            is_superuser=is_superuser,
            last_login=now,
            date_joined=now,
            **extra_fields,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, False, False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, True, True, **extra_fields)


class Profile(AbstractBaseUser, PermissionsMixin):
    """
    Profile model, replaces user model and extends with photo, frontend,backend, year_started_learning,company
    and replaces username with email
    """

    name = models.CharField(max_length=100)
    photo = models.URLField()
    email = models.EmailField(unique=True)
    frontend = models.TextField()
    backend = models.TextField()
    year_started_learning = models.IntegerField(
        _("year_started_learning"), choices=year_choices, default=datetime.datetime.now().year
    )
    company = models.TextField()
    is_staff = models.BooleanField(
        _("staff status"), default=False, help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)
    objects = ProfileManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return "{0.name} - {0.email}".format(self)

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def get_absolute_url(self):
        return "/users/%s/" % urlquote(self.email)

    def get_full_name(self):
        full_name = "%s" % self.name
        return full_name.strip()

    def get_short_name(self):
        return self.name
