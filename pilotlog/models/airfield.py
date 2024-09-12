"""Airfield model."""
from django.db import models


class Airfield(models.Model):
    af_code = models.CharField(
        max_length=255, primary_key=True,
        verbose_name="AFCode",
        help_text="Unique identifier for the airfield"
    )
    af_cat = models.IntegerField(
        verbose_name="AFCat",
        help_text="Category of the airfield"
    )
    af_country = models.IntegerField(
        verbose_name="AFCountry",
        help_text="Country code of the airfield"
    )
    af_iata = models.CharField(
        max_length=3,
        verbose_name="AFIATA",
        help_text="IATA code of the airfield"
    )
    af_icao = models.CharField(
        max_length=4,
        verbose_name="AFICAO",
        help_text="ICAO code of the airfield"
    )
    af_name = models.CharField(
        max_length=255,
        verbose_name="AFName",
        help_text="Name of the airfield"
    )
    elevation_ft = models.IntegerField(
        verbose_name="ElevationFT",
        help_text="Elevation of the airfield in feet"
    )
    latitude = models.IntegerField(
        verbose_name="Latitude",
        help_text="Latitude coordinate of the airfield"
    )
    longitude = models.IntegerField(
        verbose_name="Longitude",
        help_text="Longitude coordinate of the airfield"
    )
    notes_user = models.TextField(
        verbose_name="NotesUser",
        help_text="Additional notes about the airfield"
    )
    region_user = models.IntegerField(
        verbose_name="RegionUser",
        help_text="User-defined region for the airfield"
    )
    show_list = models.BooleanField(
        verbose_name="ShowList",
        help_text="Whether to display the airfield in lists"
    )
    tz_code = models.IntegerField(
        verbose_name="TZCode",
        help_text="Time zone code for the airfield"
    )

    def __str__(self):
        return str(self.af_code)
