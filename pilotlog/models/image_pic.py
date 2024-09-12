from django.db import models
from .bases import RecordTracking


class ImagePic(RecordTracking):
    img_code = models.CharField(
        max_length=255,
        primary_key=True,
        verbose_name="ImgCode",
        help_text="Unique identifier for the image"
    )
    file_ext = models.CharField(
        max_length=10,
        verbose_name="FileExt",
        help_text="File extension of the image"
    )
    file_name = models.CharField(
        max_length=255,
        verbose_name="FileName",
        help_text="Name of the image file"
    )
    img_download = models.BooleanField(
        default=False,
        verbose_name="Img_Download",
        help_text="Indicates if the image has been downloaded"
    )
    img_upload = models.BooleanField(
        default=False,
        verbose_name="Img_Upload",
        help_text="Indicates if the image has been uploaded"
    )
    link_code = models.CharField(
        max_length=255,
        verbose_name="LinkCode",
        help_text="Code linking the image to other records"
    )

    class Meta:
        verbose_name = "ImagePic"
        verbose_name_plural = "ImagePics"

    def __str__(self):
        return self.img_code
