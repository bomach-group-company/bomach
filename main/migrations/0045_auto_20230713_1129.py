# Generated by Django 3.2.18 on 2023-07-13 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0044_auto_20230712_1010'),
    ]

    operations = [
        migrations.AddField(
            model_name='propertycoordinates',
            name='zone',
            field=models.IntegerField(default='32', max_length=50),
        ),
        migrations.AlterField(
            model_name='propertycoordinates',
            name='property',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='coordinates', to='main.property'),
        ),
        migrations.AlterField(
            model_name='propertyimage',
            name='property',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='main.property'),
        ),
    ]
