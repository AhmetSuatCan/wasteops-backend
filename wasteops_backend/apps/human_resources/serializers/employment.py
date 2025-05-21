from rest_framework import serializers
from apps.human_resources.models import Employment, OrganizationJoinCode
from django.utils import timezone

'''
These two serializers is for generating a joining code to create an Employment.

An employment is basically a connection between a User and Organization.
'''


class GenerateJoinCodeSerializer(serializers.Serializer):
    def create(self, validated_data):
        user = self.context['request'].user
        organization = user.organizations.first()

        code = OrganizationJoinCode.generate_code()
        return OrganizationJoinCode.objects.create(
            code=code,
            organization=organization,
            created_by=user,
        )


class UseJoinCodeSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=6, write_only=True)

    def validate_code(self, code):
        try:
            join_code = OrganizationJoinCode.objects.get(code=code)
        except OrganizationJoinCode.DoesNotExist:
            raise serializers.ValidationError("Invalid join code.")

        if not join_code.is_valid():
            raise serializers.ValidationError("Join code is expired or revoked.")

        self.join_code = join_code
        return code

    def validate(self, attrs):
        user = self.context['request'].user

        if Employment.objects.filter(user=user, end_date__isnull=True).exists():
            raise serializers.ValidationError("User is already employed.")

        return attrs

    def create(self, validated_data):
        user = self.context['request'].user
        join_code = self.join_code

        employment = Employment.objects.create(
            user=user,
            organization=join_code.organization,
            start_date=timezone.now()
        )
        return employment


class OrganizationJoinCodeListSerializer(serializers.ModelSerializer):
    organization_name = serializers.CharField(source='organization.name', read_only=True)
    created_by_username = serializers.CharField(source='created_by.username', read_only=True)
    is_valid = serializers.SerializerMethodField()

    class Meta:
        model = OrganizationJoinCode
        fields = [
            'code',
            'organization_name',
            'created_by_username',
            'created_at',
            'expires_at',
            'is_revoked',
            'is_valid'
        ]

    def get_is_valid(self, obj):
        return obj.is_valid()
