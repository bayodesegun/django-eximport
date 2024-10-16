"""PilotLog model."""
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.db import models

from ._bases import TrackedRecord

User = get_user_model()


class PilotLog(TrackedRecord):
    guid = models.CharField(
        primary_key=True, max_length=255,
        verbose_name="guid",
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
        verbose_name="platform",
        help_text="The platform this record belongs to"
    )
    table = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.CharField(
        max_length=255,
        verbose_name="object_id",
        help_text="The id of the object this record belongs to"
    )
    meta = GenericForeignKey("table", "object_id")

    class Meta:
        verbose_name = "Pilot Log"
        verbose_name_plural = "Pilot Logs"

    def __str__(self):
        return f"PilotLog {self.id} by {self.user_id}"

    @classmethod
    def process_for_storage(cls, data):
        processed_data = super().process_for_storage(data)
        processed_data['table_id'] = data.get('table').lower()

        return processed_data
