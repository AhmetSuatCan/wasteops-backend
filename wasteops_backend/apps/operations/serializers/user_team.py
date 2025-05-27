from rest_framework import serializers
from apps.operations.models import UserTeam
from apps.users.serializers import UserMiniSerializer


class UserTeamSerializer(serializers.ModelSerializer):
    employment_id = serializers.PrimaryKeyRelatedField(
        queryset=UserTeam._meta.get_field('employment').related_model.objects.all(),
        source='employment'
    )
    team_id = serializers.PrimaryKeyRelatedField(
        queryset=UserTeam._meta.get_field('team').related_model.objects.all(),
        source='team'
    )
    user = serializers.SerializerMethodField()

    class Meta:
        model = UserTeam
        fields = [
            'id',
            'employment_id',
            'user',
            'team_id',
            'role',
            'assigned_at',
            'removed_at',
        ]
        read_only_fields = ['assigned_at', 'removed_at', 'user']

    def get_user(self, obj):
        return UserMiniSerializer(obj.employment.user).data
