from rest_framework import serializers
from apps.maps.models import Container


class ContainerSerializer(serializers.ModelSerializer):
    organization = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Container
        fields = ['id', 'name', 'address', 'latitude', 'longitude', 'organization', 'created_at']
        read_only_fields = ['id', 'created_at', 'organization']

    def create(self, validated_data):
        user = self.context['request'].user
        organization = user.organizations.first()
        validated_data['organization'] = organization
        return super().create(validated_data)
