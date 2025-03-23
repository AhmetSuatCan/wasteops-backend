from django.contrib.auth.models import AbstractUser
from django.db import models


class UserModel(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=10,
                              choices=[('M', 'Male'),
                                       ('F', 'Female'),
                                       ('O', 'Other')])
    age = models.PositiveIntegerField()
    role = models.CharField(max_length=10, choices=[('A', 'Admin'),
                                                    ('E', 'Employee')])
    phone_number = models.CharField(max_length=15)
    address = models.TextField()

    # Override the default username field to use email
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email
