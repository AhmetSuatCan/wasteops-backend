from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
import uuid


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        extra_fields.setdefault('is_active', True)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)  # Hashes password
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=10,
                              choices=[('M', 'Male'),
                                       ('F', 'Female'),
                                       ('O', 'Other')])
    age = models.PositiveIntegerField()
    role = models.CharField(max_length=10, choices=[('A', 'Admin'),
                                                    ('E', 'Employee')])
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    # Override the default username field to use email
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name',
                       'gender',
                       'age',
                       'role',
                       'phone_number',
                       'address']

    def __str__(self):
        return self.email
