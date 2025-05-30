from django.db import models
from django.utils import timezone


class ShiftModel(models.Model):
    # TODO: A status enum field => Pending | started | finished
    # We may be able do derive status from end_time and start_time and from timezone.now but we need to define
    # the difference between a Shift that must be started and a Shift has actually started
    name = models.CharField(max_length=255, default='unnamed')
    route = models.ForeignKey(
        "maps.Route",
        on_delete=models.CASCADE,
        related_name="shifts"
    )
    team = models.ForeignKey(
        "operations.Team",
        on_delete=models.CASCADE,
        related_name="shifts"
    )
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(null=True)
    organization = models.ForeignKey(
        "organizations.Organization",
        on_delete=models.CASCADE,
        related_name="shifts"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('route', 'team', 'start_time')
