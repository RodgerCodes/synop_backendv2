# Generated by Django 4.1 on 2023-03-21 08:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user_account', '0005_station_district'),
    ]

    operations = [
        migrations.AddField(
            model_name='station',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='station',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
