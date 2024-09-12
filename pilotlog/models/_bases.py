"""Base models for all models in the application."""
from django.db import models


class TrackedRecord(models.Model):
    record_modified = models.DateTimeField(
        auto_now=True,
        verbose_name='RecordModified',
        help_text='Date and time of last modification to record'
    )

    class Meta:
        abstract = True

    @classmethod
    def process_for_storage(cls, data):
        """
        Processes data for storage in the database.

        As the data fields may not correspond to the database fields,
        we need to map the data fields to the database fields.
        """
        kwargs = {}
        for field in cls._meta.fields:
            if field.verbose_name in data:
                kwargs[field.name] = data[field.verbose_name]

        return kwargs
