from django.db import models


class Aircraft(models.Model):
    aircraft_code = models.CharField(
        primary_key=True, max_length=255,
        help_text="Unique identifier for the aircraft"
    )
    active = models.BooleanField(
        default=False,
        help_text="Indicates if the aircraft is currently active"
    )
    aerobatic = models.BooleanField(
        default=False,
        help_text="Indicates if the aircraft is capable of aerobatic maneuvers"
    )
    category = models.IntegerField(
        blank=False, null=False,
        help_text="Category of the aircraft"
    )
    aircraft_class = models.IntegerField(
        blank=False, null=False,
        help_text="Class of the aircraft"
    )
    company = models.CharField(
        max_length=255, blank=False,
        help_text="Company or manufacturer of the aircraft"
    )
    complex = models.BooleanField(
        default=False,
        help_text="Indicates if the aircraft is classified as complex"
    )
    cond_log = models.IntegerField(
        null=False, blank=False,
        help_text="Condition log number"
    )
    default_app = models.IntegerField(
        null=False, blank=False,
        help_text="Default approach setting"
    )
    default_launch = models.IntegerField(
        null=False, blank=False,
        help_text="Default launch setting"
    )
    default_log = models.IntegerField(
        null=False, blank=False,
        help_text="Default log setting"
    )
    default_ops = models.IntegerField(
        null=False, blank=False,
        help_text="Default operations setting"
    )
    device_code = models.IntegerField(
        null=False, blank=False,
        help_text="Code for the device associated with the aircraft"
    )
    efis = models.BooleanField(
        default=False,
        help_text="Indicates if the aircraft has Electronic Flight Instrument System"
    )
    f_n_p_t = models.IntegerField(
        default=0,
        help_text="Flight and Navigation Procedures Trainer level"
    )
    fav_list = models.BooleanField(
        default=False,
        help_text="Indicates if the aircraft is in the favorite list"
    )
    fin = models.CharField(
        max_length=255, blank=True,
        help_text="Financial or other identifier"
    )
    high_perf = models.BooleanField(
        default=False,
        help_text="Indicates if the aircraft is classified as high performance"
    )
    kg5700 = models.BooleanField(
        default=False,
        help_text="Indicates if the aircraft is over 5700 kg"
    )
    make = models.CharField(
        max_length=255, blank=False,
        help_text="Make of the aircraft"
    )
    model = models.CharField(
        max_length=255, blank=False,
        help_text="Model of the aircraft"
    )
    power = models.IntegerField(
        default=1,
        help_text="Power rating of the aircraft"
    )
    rating = models.CharField(
        max_length=255, blank=True,
        help_text="Rating of the aircraft"
    )
    ref_search = models.CharField(
        max_length=255, blank=False,
        help_text="Reference for search purposes"
    )
    reference = models.CharField(
        max_length=255,
        help_text="Reference identifier for the aircraft"
    )
    run2 = models.BooleanField(
        default=False,
        help_text="Indicates if the aircraft has a second engine or run capability"
    )
    sea = models.BooleanField(
        default=False,
        help_text="Indicates if the aircraft is sea-capable"
    )
    seats = models.IntegerField(
        blank=False, null=False,
        help_text="Number of seats in the aircraft"
    )
    sub_model = models.CharField(
        max_length=255, blank=True,
        help_text="Sub-model of the aircraft"
    )
    t_m_g = models.BooleanField(
        default=False,
        help_text="Indicates if the aircraft is a Touring Motor Glider"
    )
    tail_wheel = models.BooleanField(
        default=False,
        help_text="Indicates if the aircraft has a tailwheel configuration"
    )

    def __str__(self):
        return f"Aircarft {self.make} {self.model}"

    class Meta:
        verbose_name = "Aircraft"
        verbose_name_plural = "Aircraft"
