# Generated by Django 5.1.1 on 2024-09-12 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pilotlog', '0011_qualification'),
    ]

    operations = [
        migrations.CreateModel(
            name='SettingConfig',
            fields=[
                ('record_modified', models.DateTimeField(auto_now=True, help_text='Date and time of last modification to record', verbose_name='RecordModified')),
                ('config_code', models.IntegerField(help_text='Unique identifier for the configuration setting', primary_key=True, serialize=False, verbose_name='ConfigCode')),
                ('data', models.TextField(blank=True, help_text='Data associated with the configuration setting', verbose_name='Data')),
                ('group', models.CharField(help_text='Group to which the configuration setting belongs', max_length=255, verbose_name='Group')),
                ('name', models.CharField(help_text='Name of the configuration setting', max_length=255, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Setting Configuration',
                'verbose_name_plural': 'Setting Configurations',
            },
        ),
    ]
