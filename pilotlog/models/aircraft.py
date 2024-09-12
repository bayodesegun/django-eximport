"""Airfield model."""
from django.db import models
from ._bases import TrackedRecord


class Aircraft(TrackedRecord):
    aircraft_code = models.CharField(
        primary_key=True, max_length=255,
        verbose_name="AircraftCode",
        help_text="Unique identifier for the aircraft"
    )
    active = models.BooleanField(
        default=False,
        verbose_name="Active",
        help_text="Indicates if the aircraft is currently active"
    )
    aerobatic = models.BooleanField(
        default=False,
        verbose_name="Aerobatic",
        help_text="Indicates if the aircraft is capable of aerobatic maneuvers"
    )
    category = models.IntegerField(
        blank=False, null=False,
        verbose_name="Category",
        help_text="Category of the aircraft"
    )
    aircraft_class = models.IntegerField(
        blank=False, null=False,
        verbose_name="Class",
        help_text="Class of the aircraft"
    )
    company = models.CharField(
        max_length=255, blank=False,
        verbose_name="Company",
        help_text="Company or manufacturer of the aircraft"
    )
    complex = models.BooleanField(
        default=False,
        verbose_name="Complex",
        help_text="Indicates if the aircraft is classified as complex"
    )
    cond_log = models.IntegerField(
        null=False, blank=False,
        verbose_name="CondLog",
        help_text="Condition log number"
    )
    default_app = models.IntegerField(
        null=False, blank=False,
        verbose_name="DefaultApp",
        help_text="Default approach setting"
    )
    default_launch = models.IntegerField(
        null=False, blank=False,
        verbose_name="DefaultLaunch",
        help_text="Default launch setting"
    )
    default_log = models.IntegerField(
        null=False, blank=False,
        verbose_name="DefaultLog",
        help_text="Default log setting"
    )
    default_ops = models.IntegerField(
        null=False, blank=False,
        verbose_name="DefaultOps",
        help_text="Default operations setting"
    )
    device_code = models.IntegerField(
        null=False, blank=False,
        verbose_name="DeviceCode",
        help_text="Code for the device associated with the aircraft"
    )
    efis = models.BooleanField(
        default=False,
        verbose_name="Efis",
        help_text="Indicates if the aircraft has Electronic Flight Instrument System"
    )
    fnpt = models.IntegerField(
        default=0,
        verbose_name="FNPT",
        help_text="Flight and Navigation Procedures Trainer level"
    )
    fav_list = models.BooleanField(
        default=False,
        verbose_name="FavList",
        help_text="Indicates if the aircraft is in the favorite list"
    )
    fin = models.CharField(
        max_length=255, blank=True,
        verbose_name="Fin",
        help_text="Financial or other identifier"
    )
    high_perf = models.BooleanField(
        default=False,
        verbose_name="HighPerf",
        help_text="Indicates if the aircraft is classified as high performance"
    )
    kg5700 = models.BooleanField(
        default=False,
        verbose_name="Kg5700",
        help_text="Indicates if the aircraft is over 5700 kg"
    )
    make = models.CharField(
        max_length=255, blank=False,
        verbose_name="Make",
        help_text="Make of the aircraft"
    )
    model = models.CharField(
        max_length=255, blank=False,
        verbose_name="Model",
        help_text="Model of the aircraft"
    )
    power = models.IntegerField(
        default=1,
        verbose_name="Power",
        help_text="Power rating of the aircraft"
    )
    rating = models.CharField(
        max_length=255, blank=True,
        verbose_name="Rating",
        help_text="Rating of the aircraft"
    )
    ref_search = models.CharField(
        max_length=255, blank=False,
        verbose_name="RefSearch",
        help_text="Reference for search purposes"
    )
    reference = models.CharField(
        max_length=255, blank=False,
        verbose_name="Reference",
        help_text="Reference identifier for the aircraft"
    )
    run2 = models.BooleanField(
        default=False,
        verbose_name="Run2",
        help_text="Indicates if the aircraft has a second engine or run capability"
    )
    sea = models.BooleanField(
        default=False,
        verbose_name="Sea",
        help_text="Indicates if the aircraft is sea-capable"
    )
    seats = models.IntegerField(
        blank=False, null=False,
        verbose_name="Seats",
        help_text="Number of seats in the aircraft"
    )
    sub_model = models.CharField(
        max_length=255, blank=True,
        verbose_name="SubModel",
        help_text="Sub-model of the aircraft"
    )
    tmg = models.BooleanField(
        default=False,
        verbose_name="TMG",
        help_text="Indicates if the aircraft is a Touring Motor Glider"
    )
    tail_wheel = models.BooleanField(
        default=False,
        verbose_name="TailWheel",
        help_text="Indicates if the aircraft has a tailwheel configuration"
    )

    class Meta:
        verbose_name = "Aircraft"
        verbose_name_plural = "Aircraft"

    def __str__(self):
        return f"{self.aircraft_code}"
