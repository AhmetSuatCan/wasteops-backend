from rest_framework import serializers
from apps.operations.models import Team


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'name', 'status', 'created_at', 'disband_date', 'organization']
        read_only_fields = ['created_at', 'organization']
