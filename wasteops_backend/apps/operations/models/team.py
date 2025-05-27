from django.db import models


class Team(models.Model):
    STATUS_CHOICES = [
        ('onShift', 'On Shift'),
        ('inactive', 'Inactive'),
    ]

    name = models.CharField(max_length=100)
    organization = models.ForeignKey(
        "organizations.Organization",
        on_delete=models.CASCADE,
        related_name="teams"
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='inactive')
    created_at = models.DateTimeField(auto_now_add=True)
    disband_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Determine if this is a disband operation
        disbanding_now = self.disband_date and not Team.objects.filter(pk=self.pk, disband_date__isnull=False).exists()

        super().save(*args, **kwargs)

        # Auto-remove employees if team is being disbanded
        if disbanding_now:
            self.members.filter(removed_at__isnull=True).update(removed_at=self.disband_date or timezone.now())
