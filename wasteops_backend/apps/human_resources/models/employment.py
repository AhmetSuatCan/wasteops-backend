# apps.human_resources.models

from django.conf import settings
from django.db import models
from django.db.models import Q
from django.utils import timezone


class Employment(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="employments"
    )
    organization = models.ForeignKey(
        "organizations.Organization",
        on_delete=models.CASCADE,
        related_name="employments"
    )
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(null=True, blank=True)

    # Optional: Who created this employment (useful for admin-audit)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="employments_created"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user"],
                condition=Q(end_date__isnull=True),
                name="only_one_active_employment_per_user"
            )
        ]
        ordering = ["-start_date"]

    def __str__(self):
        return f"{self.user} @ {self.organization} ({'active' if self.current_state else 'ended'})"

    @property
    def is_active(self):
        return self.end_date is None

    @classmethod
    def user_has_active_employment(cls, user):
        return cls.objects.filter(user=user, end_date__isnull=True).exists()

    def end_employment(self, when=None):
        if self.end_date is not None:
            return
        self.end_date = when or timezone.now()
        self.save()
