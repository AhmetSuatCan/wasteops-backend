# apps.operations.serializers.shift_progress.py

from rest_framework import serializers
from apps.operations.models import ShiftProgressModel


class ShiftProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShiftProgressModel
        fields = ['id', 'shift', 'route_node', 'status', 'updated_at']
        read_only_fields = ['updated_at']
