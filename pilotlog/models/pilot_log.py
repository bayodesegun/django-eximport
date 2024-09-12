"""PilotLog model."""
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.db import models

from .bases import RecordTracking

User = get_user_model()


class PilotLog(RecordTracking):
    guid = models.CharField(
        primary_key=True, max_length=255,
        verbose_name="GUID",
        help_text="The unique identifier for this record"
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        blank=False, null=False,
        verbose_name="User",
        help_text="The user who logged this record"
    )
    platform = models.IntegerField(
        blank=False, null=False, db_index=True,
        verbose_name="Platform",
        help_text="The platform this record belongs to"
    )
    table = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.CharField(
        max_length=255,
        help_text="The id of the object this record belongs to"
    )
    meta = GenericForeignKey("table", "object_id")

    def __str__(self):
        return f"PilotLog {self.id} by {self.user_id}"

    class Meta:
        verbose_name = "Pilot Log"
        verbose_name_plural = "Pilot Logs"
