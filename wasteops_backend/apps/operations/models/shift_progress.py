from django.db import models


class ShiftProgressModel(models.Model):
    shift = models.ForeignKey(
        "operations.ShiftModel",
        on_delete=models.CASCADE,
        related_name="progress_entries"
    )
    route_node = models.ForeignKey(
        "maps.RouteNode",
        on_delete=models.CASCADE,
        related_name="shift_progress"
    )
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('collected', 'Collected'),
        ('skipped', 'Skipped'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('shift', 'route_node')
