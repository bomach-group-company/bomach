# Generated by Django 3.2.18 on 2023-07-11 07:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0041_auto_20230711_0835'),
    ]

    operations = [
        migrations.RenameField(
            model_name='propertycoordinates',
            old_name='east',
            new_name='easting',
        ),
        migrations.RenameField(
            model_name='propertycoordinates',
            old_name='north',
            new_name='northing',
        ),
    ]
