# Generated by Django 5.1.1 on 2024-09-12 05:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pilotlog', '0002_aircraft'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aircraft',
            name='f_n_p_t',
        ),
        migrations.RemoveField(
            model_name='aircraft',
            name='t_m_g',
        ),
        migrations.AddField(
            model_name='aircraft',
            name='fnpt',
            field=models.IntegerField(default=0, help_text='Flight and Navigation Procedures Trainer level', verbose_name='FNPT'),
        ),
        migrations.AddField(
            model_name='aircraft',
            name='tmg',
            field=models.BooleanField(default=False, help_text='Indicates if the aircraft is a Touring Motor Glider', verbose_name='TMG'),
        ),
        migrations.AlterField(
            model_name='aircraft',
            name='active',
            field=models.BooleanField(default=False, help_text='Indicates if the aircraft is currently active', verbose_name='Active'),
        ),
        migrations.AlterField(
            model_name='aircraft',
            name='aerobatic',
            field=models.BooleanField(default=False, help_text='Indicates if the aircraft is capable of aerobatic maneuvers', verbose_name='Aerobatic'),
        ),
        migrations.AlterField(
            model_name='aircraft',
            name='aircraft_class',
            field=models.IntegerField(help_text='Class of the aircraft', verbose_name='Class'),
        ),
        migrations.AlterField(
            model_name='aircraft',
            name='aircraft_code',
            field=models.CharField(help_text='Unique identifier for the aircraft', max_length=255, primary_key=True, serialize=False, verbose_name='AircraftCode'),
        ),
        migrations.AlterField(
            model_name='aircraft',
            name='category',
            field=models.IntegerField(help_text='Category of the aircraft', verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='aircraft',
            name='company',
            field=models.CharField(help_text='Company or manufacturer of the aircraft', max_length=255, verbose_name='Company'),
        ),
        migrations.AlterField(
            model_name='aircraft',
            name='complex',
            field=models.BooleanField(default=False, help_text='Indicates if the aircraft is classified as complex', verbose_name='Complex'),
        ),
        migrations.AlterField(
            model_name='aircraft',
            name='cond_log',
            field=models.IntegerField(help_text='Condition log number', verbose_name='CondLog'),
        ),
        migrations.AlterField(
            model_name='aircraft',
            name='default_app',
            field=models.IntegerField(help_text='Default approach setting', verbose_name='DefaultApp'),
        ),
        migrations.AlterField(
            model_name='aircraft',
            name='default_launch',
            field=models.IntegerField(help_text='Default launch setting', verbose_name='DefaultLaunch'),
        ),
        migrations.AlterField(
            model_name='aircraft',
            name='default_log',
            field=models.IntegerField(help_text='Default log setting', verbose_name='DefaultLog'),
        ),
        migrations.AlterField(
            model_name='aircraft',
            name='default_ops',
            field=models.IntegerField(help_text='Default operations setting', verbose_name='DefaultOps'),
        ),
        migrations.AlterField(
            model_name='aircraft',
            name='device_code',
            field=models.IntegerField(help_text='Code for the device associated with the aircraft', verbose_name='DeviceCode'),
        ),
        migrations.AlterField(
            model_name='aircraft',
            name='efis',
            field=models.BooleanField(default=False, help_text='Indicates if the aircraft has Electronic Flight Instrument System', verbose_name='Efis'),
        ),
        migrations.AlterField(
            model_name='aircraft',
            name='fav_list',
            field=models.BooleanField(default=False, help_text='Indicates if the aircraft is in the favorite list', verbose_name='FavList'),
        ),
        migrations.AlterField(
            model_name='aircraft',
            name='fin',
            field=models.CharField(blank=True, help_text='Financial or other identifier', max_length=255, verbose_name='Fin'),
        ),
        migrations.AlterField(
            model_name='aircraft',
            name='high_perf',
            field=models.BooleanField(default=False, help_text='Indicates if the aircraft is classified as high performance', verbose_name='HighPerf'),
        ),
        migrations.AlterField(
            model_name='aircraft',
            name='kg5700',
            field=models.BooleanField(default=False, help_text='Indicates if the aircraft is over 5700 kg', verbose_name='Kg5700'),
        ),
        migrations.AlterField(
            model_name='aircraft',
            name='make',
            field=models.CharField(help_text='Make of the aircraft', max_length=255, verbose_name='Make'),
        ),
        migrations.AlterField(
            model_name='aircraft',
            name='model',
            field=models.CharField(help_text='Model of the aircraft', max_length=255, verbose_name='Model'),
        ),
        migrations.AlterField(
            model_name='aircraft',
            name='power',
            field=models.IntegerField(default=1, help_text='Power rating of the aircraft', verbose_name='Power'),
        ),
        migrations.AlterField(
            model_name='aircraft',
            name='rating',
            field=models.CharField(blank=True, help_text='Rating of the aircraft', max_length=255, verbose_name='Rating'),
        ),
        migrations.AlterField(
            model_name='aircraft',
            name='record_modified',
            field=models.DateTimeField(auto_now=True, help_text='Date and time of last modification to record', verbose_name='RecordModified'),
        ),
        migrations.AlterField(
            model_name='aircraft',
            name='ref_search',
            field=models.CharField(help_text='Reference for search purposes', max_length=255, verbose_name='RefSearch'),
        ),
        migrations.AlterField(
            model_name='aircraft',
            name='reference',
            field=models.CharField(help_text='Reference identifier for the aircraft', max_length=255, verbose_name='Reference'),
        ),
        migrations.AlterField(
            model_name='aircraft',
            name='run2',
            field=models.BooleanField(default=False, help_text='Indicates if the aircraft has a second engine or run capability', verbose_name='Run2'),
        ),
        migrations.AlterField(
            model_name='aircraft',
            name='sea',
            field=models.BooleanField(default=False, help_text='Indicates if the aircraft is sea-capable', verbose_name='Sea'),
        ),
        migrations.AlterField(
            model_name='aircraft',
            name='seats',
            field=models.IntegerField(help_text='Number of seats in the aircraft', verbose_name='Seats'),
        ),
        migrations.AlterField(
            model_name='aircraft',
            name='sub_model',
            field=models.CharField(blank=True, help_text='Sub-model of the aircraft', max_length=255, verbose_name='SubModel'),
        ),
        migrations.AlterField(
            model_name='aircraft',
            name='tail_wheel',
            field=models.BooleanField(default=False, help_text='Indicates if the aircraft has a tailwheel configuration', verbose_name='TailWheel'),
        ),
        migrations.AlterField(
            model_name='pilotlog',
            name='guid',
            field=models.CharField(help_text='The unique identifier for this record', max_length=255, primary_key=True, serialize=False, verbose_name='GUID'),
        ),
        migrations.AlterField(
            model_name='pilotlog',
            name='platform',
            field=models.IntegerField(db_index=True, help_text='The platform this record belongs to', verbose_name='Platform'),
        ),
        migrations.AlterField(
            model_name='pilotlog',
            name='record_modified',
            field=models.DateTimeField(auto_now=True, help_text='Date and time of last modification to record', verbose_name='RecordModified'),
        ),
        migrations.AlterField(
            model_name='pilotlog',
            name='user',
            field=models.ForeignKey(help_text='The user who logged this record', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
    ]
