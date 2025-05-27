# serializers/route_node.py
from rest_framework import serializers
from apps.maps.models import Route, RouteNode, Container


class RouteNodeWriteSerializer(serializers.Serializer):
    container_id = serializers.PrimaryKeyRelatedField(queryset=Container.objects.all())
    order = serializers.IntegerField(min_value=1)


class RouteNodeBulkCreateSerializer(serializers.Serializer):
    route_id = serializers.PrimaryKeyRelatedField(queryset=Route.objects.all())
    nodes = RouteNodeWriteSerializer(many=True)

    def create(self, validated_data):
        route = validated_data['route_id']
        nodes_data = validated_data['nodes']
        route_nodes = []

        for node in nodes_data:
            route_nodes.append(RouteNode(
                route=route,
                container=node['container_id'],
                order=node['order']
            ))

        return RouteNode.objects.bulk_create(route_nodes)
