# Generated by Django 3.2.18 on 2023-07-13 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0045_auto_20230713_1129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propertycoordinates',
            name='zone',
            field=models.IntegerField(default=32),
        ),
    ]
