# Generated by Django 4.1 on 2022-08-24 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('codes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='synop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=1000, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('data', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='codes.data')),
            ],
        ),
    ]