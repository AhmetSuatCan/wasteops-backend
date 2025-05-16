from django.conf import settings
from django.db import models


# Organization core model:

class Organization(models.Model):
    GOVERNMENT = 'government'
    PRIVATE = 'private'

    ORGANIZATION_TYPE_CHOICES = [
        (GOVERNMENT, 'Government'),
        (PRIVATE, 'Private'),
    ]

    name = models.CharField(max_length=255)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='organizations'
    )
    address = models.CharField(max_length=500)
    organization_type = models.CharField(max_length=20,
                                         choices=ORGANIZATION_TYPE_CHOICES)
    num_of_facilities = models.IntegerField(default=0)
    num_of_cars = models.IntegerField(default=0)
    num_of_containers = models.IntegerField(default=0)

    def __str__(self):
        return self.name


# Facility Model

class Facility(models.Model):
    RECYCLING = 'recycling'
    TREATMENT = 'treatment'
    FACILITY_TYPE_CHOICES = [
        (RECYCLING, 'Recycling'),
        (TREATMENT, 'Waste Treatment'),
    ]
    name = models.CharField(max_length=255)
    facility_type = models.CharField(max_length=20,
                                     choices=FACILITY_TYPE_CHOICES)
    address = models.CharField(max_length=500)
    capacity = models.IntegerField()  # Max capacity (in tons, liters, etc.)
    contact_info = models.CharField(max_length=255, blank=True, null=True)
    operating_hours = models.CharField(max_length=100, blank=True, null=True)
    organization = models.ForeignKey('Organization', on_delete=models.CASCADE, related_name='facilities')

    def __str__(self):
        return self.name


# Car Model

class Car(models.Model):
    TRUCK = 'truck'
    VAN = 'van'

    CAR_TYPE_CHOICES = [
        (TRUCK, 'Truck'),
        (VAN, 'Van'),
    ]

    license_plate = models.CharField(max_length=50, unique=True)
    car_type = models.CharField(max_length=20, choices=CAR_TYPE_CHOICES)
    capacity = models.IntegerField()  # Max capacity (in tons, liters, etc.)
    status = models.CharField(max_length=20)  # Available, In Service, etc.
    location = models.CharField(max_length=255)  # Current location
    organization = models.ForeignKey('Organization', on_delete=models.CASCADE,
                                     related_name='cars')

    def __str__(self):
        return f"{self.car_type} - {self.license_plate}"


# Waste Container Model

class WasteContainer(models.Model):
    BIN = 'bin'
    DUMPSTER = 'dumpster'

    CONTAINER_TYPE_CHOICES = [
        (BIN, 'Bin'),
        (DUMPSTER, 'Dumpster'),
    ]

    container_id = models.CharField(max_length=50, unique=True)
    container_type = models.CharField(max_length=20,
                                      choices=CONTAINER_TYPE_CHOICES)
    capacity = models.IntegerField()  # Max capacity (in tons, liters, etc.)
    location = models.CharField(max_length=500)  # The physical location
    status = models.CharField(max_length=20)  # Full, Empty, In Use, etc.
    organization = models.ForeignKey('Organization', on_delete=models.CASCADE,
                                     related_name='waste_containers')

    def __str__(self):
        return f"{self.container_type} - {self.container_id}"
