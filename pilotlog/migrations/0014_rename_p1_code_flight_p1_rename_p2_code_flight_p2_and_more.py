# Generated by Django 5.1.1 on 2024-09-12 23:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pilotlog', '0013_alter_flight_p1_code_alter_flight_p2_code_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='flight',
            old_name='p1_code',
            new_name='p1',
        ),
        migrations.RenameField(
            model_name='flight',
            old_name='p2_code',
            new_name='p2',
        ),
        migrations.RenameField(
            model_name='flight',
            old_name='p3_code',
            new_name='p3',
        ),
        migrations.RenameField(
            model_name='flight',
            old_name='p4_code',
            new_name='p4',
        ),
        migrations.RenameField(
            model_name='myquerybuild',
            old_name='mq_code',
            new_name='mq',
        ),
    ]
