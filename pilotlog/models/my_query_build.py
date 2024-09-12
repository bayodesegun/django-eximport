from django.db import models
from ._bases import TrackedRecord


class MyQueryBuild(TrackedRecord):
    mqb_code = models.CharField(
        max_length=36,
        primary_key=True,
        verbose_name="mQBCode",
        help_text="Unique identifier for the query build"
    )
    build1 = models.CharField(
        max_length=255,
        verbose_name="Build1",
        help_text="First build parameter"
    )
    build2 = models.IntegerField(
        verbose_name="Build2",
        help_text="Second build parameter"
    )
    build3 = models.IntegerField(
        verbose_name="Build3",
        help_text="Third build parameter"
    )
    build4 = models.CharField(
        max_length=255,
        verbose_name="Build4",
        help_text="Fourth build parameter"
    )
    mq = models.ForeignKey(
        "MyQuery", on_delete=models.PROTECT,
        related_name="my_query_builds",
        verbose_name="mQCode",
        db_column="mq_code",
        help_text="Associated query code"
    )

    class Meta:
        verbose_name = "My Query Build"
        verbose_name_plural = "My Query Builds"

    def __str__(self):
        return str(self.mqb_code)
