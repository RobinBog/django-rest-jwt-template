from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.utils import timezone

# to define the user class
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

# the manager for the user class
from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        return self.create_user(email, password, **extra_fields)

    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('Email must be set'))
        email = self.normalize_email(email) # normalize the email - for example: lowercasing the domain
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    # Fields of the user model
    email = models.EmailField(_('email adress'), unique=True)
    company_name = models.CharField(max_length=75, blank=True)
    register_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(_(
        'description'
    ), max_length=500, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomUserManager() # define which manager should be used

    # set the username_field which defines the unique identifier for the "user model" to "email"
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email