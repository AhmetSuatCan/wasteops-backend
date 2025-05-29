
# apps.operations.serializers.shift.py

from rest_framework import serializers
from apps.operations.models import ShiftModel


class ShiftSerializer(serializers.ModelSerializer):
    route = serializers.PrimaryKeyRelatedField(read_only=True)
    team = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = ShiftModel
        fields = ['name', 'id', 'route', 'team', 'start_time', 'organization', 'created_at', 'end_time']
        read_only_fields = ['id', 'organization', 'created_at', 'end_time']


class ShiftCreateSerializer(serializers.Serializer):
    route_id = serializers.IntegerField()
    team_id = serializers.IntegerField()
    start_time = serializers.DateTimeField(required=False)
    name = serializers.CharField(required=False, default="Unnamed Shift")
