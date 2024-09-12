"""Base models for all models in the application."""
from datetime import datetime
from django.utils import timezone
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
            db_column = field.get_attname_column()[1]
            if field.verbose_name in data:
                kwargs[db_column] = data[field.verbose_name]

        # Manually get non-conforming fields
        timestamp = data.get('Record_Modified', data.get('_modfied', None))
        if timestamp is not None:
            date_from_timestamp = datetime.fromtimestamp(timestamp)
            kwargs['record_modified'] = timezone.make_aware(
                date_from_timestamp
            )

        return kwargs
