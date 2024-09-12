from django.db import models

class RecordTracking(models.Model):
    record_modified = models.DateTimeField(
        auto_now=True,
        verbose_name='RecordModified',
        help_text='Date and time of last modification to record'
    )

    class Meta:
        abstract = True
