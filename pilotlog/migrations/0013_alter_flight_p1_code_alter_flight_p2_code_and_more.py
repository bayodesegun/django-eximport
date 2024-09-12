# Generated by Django 5.1.1 on 2024-09-12 23:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pilotlog', '0012_settingconfig'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='p1_code',
            field=models.ForeignKey(db_column='p1_code', help_text='Record for the first pilot', on_delete=django.db.models.deletion.PROTECT, related_name='p1_flights', to='pilotlog.pilot', verbose_name='P1Code'),
        ),
        migrations.AlterField(
            model_name='flight',
            name='p2_code',
            field=models.ForeignKey(db_column='p2_code', help_text='Code for the second pilot', on_delete=django.db.models.deletion.PROTECT, related_name='p2_flights', to='pilotlog.pilot', verbose_name='P2Code'),
        ),
        migrations.AlterField(
            model_name='flight',
            name='p3_code',
            field=models.ForeignKey(db_column='p3_code', help_text='Code for the third pilot', on_delete=django.db.models.deletion.PROTECT, related_name='p3_flights', to='pilotlog.pilot', verbose_name='P3Code'),
        ),
        migrations.AlterField(
            model_name='flight',
            name='p4_code',
            field=models.ForeignKey(db_column='p4_code', help_text='Code for the fourth pilot', on_delete=django.db.models.deletion.PROTECT, related_name='p4_flights', to='pilotlog.pilot', verbose_name='P4Code'),
        ),
        migrations.AlterField(
            model_name='imagepic',
            name='img_download',
            field=models.BooleanField(default=False, help_text='Indicates if the image has been downloaded', verbose_name='ImgDownload'),
        ),
        migrations.AlterField(
            model_name='imagepic',
            name='img_upload',
            field=models.BooleanField(default=False, help_text='Indicates if the image has been uploaded', verbose_name='ImgUpload'),
        ),
        migrations.AlterField(
            model_name='myquerybuild',
            name='mq_code',
            field=models.ForeignKey(db_column='mq_code', help_text='Associated query code', on_delete=django.db.models.deletion.PROTECT, related_name='my_query_builds', to='pilotlog.myquery', verbose_name='mQCode'),
        ),
        migrations.AlterField(
            model_name='pilot',
            name='certificate',
            field=models.ForeignKey(blank=True, help_text="Pilot's certificate information", null=True, on_delete=django.db.models.deletion.PROTECT, to='pilotlog.qualification', verbose_name='Certificate'),
        ),
    ]
