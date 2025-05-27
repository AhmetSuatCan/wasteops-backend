# serializers/route.py
from rest_framework import serializers
from apps.maps.serializers.container import ContainerSerializer
from apps.maps.models import Route, RouteNode


class RouteNodeReadSerializer(serializers.ModelSerializer):
    container = ContainerSerializer(read_only=True)

    class Meta:
        model = RouteNode
        fields = ['id', 'order', 'container']


class RouteSerializer(serializers.ModelSerializer):
    organization = serializers.PrimaryKeyRelatedField(read_only=True)
    created_by = serializers.PrimaryKeyRelatedField(read_only=True)
    nodes = RouteNodeReadSerializer(many=True, read_only=True)

    class Meta:
        model = Route
        fields = ['id', 'name', 'organization', 'created_by', 'created_at', 'nodes']
        read_only_fields = ['id', 'created_at', 'created_by', 'organization']
