# Generated by Django 4.1 on 2022-12-08 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('codes', '0002_synop'),
    ]

    operations = [
        migrations.AlterField(
            model_name='synop',
            name='data',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='synop_data', to='codes.data'),
        ),
    ]
