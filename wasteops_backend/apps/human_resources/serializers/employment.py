from rest_framework import serializers
from .models import Employment
from .models import OrganizationJoinCode
from time import timezone


class GenerateJoinCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationJoinCode
        fields = ['code', 'expires_at', 'created_at']

    def create(self, validated_data):
        user = self.context['request'].user
        organization = user.organization

        code = OrganizationJoinCode.generate_code()
        return OrganizationJoinCode.objects.create(
            code=code,
            organization=organization,
            created_by=user,
            expires_at=validated_data.get('expires_at')
        )


class UseJoinCodeSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=6)

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
