from rest_framework import serializers
from .models import Organization, Facility, WasteContainer, Car


# Organization Serializer

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'
        extra_kwargs = {
            'owner': {'read_only': True}
        }


# Facility Serializer:

class FacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Facility
        fields = ['id', 'name', 'facility_type', 'address', 'capacity',
                  'contact_info', 'operating_hours', 'organization']
        read_only_fields = ['organization']  # will be set automatically in views


# Waste Containers Serializer:

class WasteContainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = WasteContainer
        fields = ['id', 'container_id', 'container_type', 'capacity',
                  'location', 'status', 'organization']
        read_only_fields = ['organization']  # will be set automatically in views


# Car Serializer:

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'license_plate', 'car_type', 'capacity', 'status',
                  'location', 'organization']
        read_only_fields = ['organization']  # will be set automatically in views
