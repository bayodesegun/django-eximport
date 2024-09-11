from django.db import models

class RecordTracking(models.Model):
    record_modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
