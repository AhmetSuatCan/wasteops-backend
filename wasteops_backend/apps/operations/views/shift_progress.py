from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from apps.operations.models import ShiftProgressModel
from apps.operations.serializers.shift_progress import ShiftProgressSerializer


class ShiftProgressViewSet(viewsets.ModelViewSet):
    serializer_class = ShiftProgressSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return ShiftProgressModel.objects.none()
        user = self.request.user
        return ShiftProgressModel.objects.filter(shift__organization=user.organizations.first())
