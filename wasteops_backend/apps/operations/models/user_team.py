# apps.operations.models.py

from django.db import models
from django.utils import timezone


class UserTeam(models.Model):
    ROLE_CHOICES = [
        ('Driver', 'Driver'),
        ('TeamLeader', 'Team Leader'),
        ('Collector', 'Collector'),
    ]

    employment = models.ForeignKey(
        "human_resources.Employment",
        on_delete=models.CASCADE,
        related_name="team_memberships"
    )

    team = models.ForeignKey(
        "operations.Team",
        on_delete=models.CASCADE,
        related_name="members"
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    assigned_at = models.DateTimeField(default=timezone.now)
    removed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = ('employment', 'team', 'removed_at')

    def __str__(self):
        return f"{self.employment.user} in {self.team.name} as {self.role}"
