import random
from django.db import models
from django.conf import settings
from django.utils import timezone


class OrganizationJoinCode(models.Model):
    code = models.CharField(max_length=6, unique=True, db_index=True)
    organization = models.ForeignKey(
        "organizations.Organization",
        on_delete=models.CASCADE,
        related_name="join_codes"
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="generated_join_codes"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(null=True, blank=True)

    is_revoked = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"JoinCode({self.code}) for {self.organization.name}"

    def is_valid(self):
        """
        Returns True if the code is usable (not expired or revoked).
        """
        if self.is_revoked:
            return False
        if self.expires_at and timezone.now() > self.expires_at:
            return False
        return True

    @staticmethod
    def generate_code(length=6, max_retries=5):
        SAFE_CHARS = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789"
        for _ in range(max_retries):
            code = ''.join(random.choices(SAFE_CHARS, k=length))
            if not OrganizationJoinCode.objects.filter(code=code).exists():
                return code
        raise ValueError("Failed to generate a unique join code after multiple attempts.")
