from django.db import models
from .bases import RecordTracking


class Pilot(RecordTracking):
    pilot_code = models.CharField(
        max_length=36,
        primary_key=True,
        verbose_name="PilotCode",
        help_text="Unique identifier for the pilot"
    )
    active = models.BooleanField(
        default=True,
        verbose_name="Active",
        help_text="Indicates if the pilot is currently active"
    )
    certificate = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Certificate",
        help_text="Pilot's certificate information"
    )
    company = models.CharField(
        max_length=255,
        verbose_name="Company",
        help_text="Company or airline the pilot works for"
    )
    facebook = models.URLField(
        blank=True,
        verbose_name="Facebook",
        help_text="Pilot's Facebook profile URL"
    )
    fav_list = models.BooleanField(
        default=False,
        verbose_name="FavList",
        help_text="Indicates if the pilot is in the favorite list"
    )
    linkedin = models.URLField(
        blank=True,
        verbose_name="LinkedIn",
        help_text="Pilot's LinkedIn profile URL"
    )
    notes = models.TextField(
        blank=True,
        verbose_name="Notes",
        help_text="Additional notes about the pilot"
    )
    phone_search = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="PhoneSearch",
        help_text="Phone number search field"
    )
    pilot_email = models.EmailField(
        blank=True,
        verbose_name="PilotEMail",
        help_text="Pilot's email address"
    )
    pilot_name = models.CharField(
        max_length=255,
        verbose_name="PilotName",
        help_text="Full name of the pilot"
    )
    pilot_phone = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="PilotPhone",
        help_text="Pilot's phone number"
    )
    pilot_ref = models.CharField(
        max_length=255,
        verbose_name="PilotRef",
        help_text="Reference number for the pilot"
    )
    pilot_search = models.CharField(
        max_length=255,
        verbose_name="PilotSearch",
        help_text="Search field for the pilot"
    )
    roster_alias = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="RosterAlias",
        help_text="Alias used for roster purposes"
    )
    user_api = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="UserAPI",
        help_text="API user identifier for the pilot"
    )

    class Meta:
        verbose_name = "Pilot"
        verbose_name_plural = "Pilots"

    def __str__(self):
        return str(self.pilot_code)
