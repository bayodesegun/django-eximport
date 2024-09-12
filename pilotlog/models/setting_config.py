from django.db import models
from ._bases import TrackedRecord


class SettingConfig(TrackedRecord):
    config_code = models.IntegerField(
        primary_key=True,
        verbose_name="ConfigCode",
        help_text="Unique identifier for the configuration setting"
    )
    data = models.TextField(
        blank=True,
        verbose_name="Data",
        help_text="Data associated with the configuration setting"
    )
    group = models.CharField(
        max_length=255,
        verbose_name="Group",
        help_text="Group to which the configuration setting belongs"
    )
    name = models.CharField(
        max_length=255,
        verbose_name="Name",
        help_text="Name of the configuration setting"
    )

    class Meta:
        verbose_name = "Setting Configuration"
        verbose_name_plural = "Setting Configurations"

    def __str__(self):
        return f"{self.name} ({self.group})"
