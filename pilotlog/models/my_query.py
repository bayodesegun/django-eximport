from django.db import models
from .bases import RecordTracking


class MyQuery(RecordTracking):
    mq_code = models.CharField(
        max_length=36,
        primary_key=True,
        verbose_name="mQCode",
        help_text="Unique identifier for the query"
    )
    name = models.CharField(
        max_length=255,
        verbose_name="Name",
        help_text="Name of the query, e.g., TIME: Actual Instrument"
    )
    quick_view = models.BooleanField(
        default=False,
        verbose_name="QuickView",
        help_text="Indicates if the query is available in quick view"
    )
    short_name = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="ShortName",
        help_text="Short name or abbreviation for the query"
    )

    class Meta:
        verbose_name = "My Query"
        verbose_name_plural = "My Queries"

    def __str__(self):
        return str(self.name)
