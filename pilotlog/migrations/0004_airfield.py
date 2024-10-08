# Generated by Django 5.1.1 on 2024-09-12 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pilotlog', '0003_remove_aircraft_f_n_p_t_remove_aircraft_t_m_g_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Airfield',
            fields=[
                ('af_code', models.CharField(help_text='Unique identifier for the airfield', max_length=255, primary_key=True, serialize=False, verbose_name='AFCode')),
                ('af_cat', models.IntegerField(help_text='Category of the airfield', verbose_name='AFCat')),
                ('af_country', models.IntegerField(help_text='Country code of the airfield', verbose_name='AFCountry')),
                ('af_iata', models.CharField(help_text='IATA code of the airfield', max_length=3, verbose_name='AFIATA')),
                ('af_icao', models.CharField(help_text='ICAO code of the airfield', max_length=4, verbose_name='AFICAO')),
                ('af_name', models.CharField(help_text='Name of the airfield', max_length=255, verbose_name='AFName')),
                ('elevation_ft', models.IntegerField(help_text='Elevation of the airfield in feet', verbose_name='ElevationFT')),
                ('latitude', models.IntegerField(help_text='Latitude coordinate of the airfield', verbose_name='Latitude')),
                ('longitude', models.IntegerField(help_text='Longitude coordinate of the airfield', verbose_name='Longitude')),
                ('notes_user', models.TextField(help_text='Additional notes about the airfield', verbose_name='NotesUser')),
                ('region_user', models.IntegerField(help_text='User-defined region for the airfield', verbose_name='RegionUser')),
                ('show_list', models.BooleanField(help_text='Whether to display the airfield in lists', verbose_name='ShowList')),
                ('tz_code', models.IntegerField(help_text='Time zone code for the airfield', verbose_name='TZCode')),
            ],
        ),
    ]
