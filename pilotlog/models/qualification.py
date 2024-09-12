from django.db import models
from ._bases import TrackedRecord

class Qualification(TrackedRecord):
    q_code = models.CharField(
        max_length=36,
        primary_key=True,
        verbose_name="QCode",
        help_text="Unique identifier for the qualification"
    )
    date_issued = models.DateField(
        null=True,
        blank=True,
        verbose_name="DateIssued",
        help_text="Date when the qualification was issued"
    )
    date_valid = models.DateField(
        null=True,
        blank=True,
        verbose_name="DateValid",
        help_text="Date until which the qualification is valid"
    )
    minimum_period = models.IntegerField(
        default=90,
        verbose_name="MinimumPeriod",
        help_text="Minimum period in days for the qualification"
    )
    minimum_qty = models.IntegerField(
        default=3,
        verbose_name="MinimumQty",
        help_text="Minimum quantity required for the qualification"
    )
    notify_comment = models.TextField(
        blank=True,
        verbose_name="NotifyComment",
        help_text="Comments for notification purposes"
    )
    notify_days = models.IntegerField(
        default=14,
        verbose_name="NotifyDays",
        help_text="Number of days before expiration to send notification"
    )
    q_type_code = models.IntegerField(
        default=3,
        verbose_name="QTypeCode",
        help_text="Code representing the type of qualification"
    )
    ref_airfield = models.CharField(
        max_length=36,
        default="00000000-0000-0000-0000-000000000000",
        verbose_name="RefAirfield",
        help_text="Reference to an airfield related to the qualification"
    )
    ref_extra = models.IntegerField(
        default=0,
        verbose_name="RefExtra",
        help_text="Extra reference information for the qualification"
    )
    ref_model = models.CharField(
        max_length=255,
        default="G500",
        verbose_name="RefModel",
        help_text="Reference to a model related to the qualification"
    )
    validity = models.IntegerField(
        default=0,
        verbose_name="Validity",
        help_text="Validity status of the qualification"
    )

    class Meta:
        verbose_name = "Qualification"
        verbose_name_plural = "Qualifications"

    def __str__(self) -> str:
        return str(self.q_code)
