# Generated by Django 3.2.18 on 2023-07-10 12:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0038_property'),
    ]

    operations = [
        migrations.CreateModel(
            name='PropertyCoordinates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='N/A', max_length=250)),
                ('x', models.CharField(max_length=250)),
                ('y', models.CharField(max_length=250)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': 'Coordinate',
                'verbose_name_plural': 'Coordinates',
            },
        ),
        migrations.AddField(
            model_name='property',
            name='coordinates',
            field=models.ManyToManyField(to='main.PropertyCoordinates'),
        ),
    ]
