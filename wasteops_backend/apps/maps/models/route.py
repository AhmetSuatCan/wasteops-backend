from django.db import models
from django.conf import settings
from django.utils import timezone


class Route(models.Model):
    name = models.CharField(max_length=255)
    organization = models.ForeignKey(
        "organizations.Organization",
        on_delete=models.CASCADE,
        related_name="routes"
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="created_routes"
    )
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
