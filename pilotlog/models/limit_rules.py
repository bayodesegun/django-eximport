from django.db import models
from .bases import RecordTracking


class LimitRules(RecordTracking):
    limit_code = models.CharField(
        max_length=36,
        primary_key=True,
        verbose_name="LimitCode",
        help_text="Unique identifier for the limit rule"
    )
    l_from = models.DateField(
        verbose_name="LFrom",
        help_text="Start date of the limit rule"
    )
    l_minutes = models.IntegerField(
        verbose_name="LMinutes",
        help_text="Number of minutes for the limit rule"
    )
    l_period_code = models.IntegerField(
        verbose_name="LPeriodCode",
        help_text="Code representing the period for the limit rule"
    )
    l_to = models.DateField(
        verbose_name="LTo",
        help_text="End date of the limit rule"
    )
    l_type = models.IntegerField(
        verbose_name="LType",
        help_text="Type of the limit rule"
    )
    l_zone = models.IntegerField(
        verbose_name="LZone",
        help_text="Zone associated with the limit rule"
    )

    def __str__(self):
        return f"LimitRule {self.limit_code}"

    class Meta:
        verbose_name = "Limit Rule"
        verbose_name_plural = "Limit Rules"
