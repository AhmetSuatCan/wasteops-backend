from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.maps.serializers import RouteNodeBulkCreateSerializer
from drf_yasg.utils import swagger_auto_schema


class RouteNodeBulkCreateAPIView(APIView):
    @swagger_auto_schema(request_body=RouteNodeBulkCreateSerializer)
    def post(self, request, *args, **kwargs):

        serializer = RouteNodeBulkCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"detail": "Route nodes created successfully."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
