# Generated by Django 4.1.4 on 2022-12-21 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_location_check_in_alter_location_check_out_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='check_in',
            field=models.DateTimeField(default='2022-12-22', verbose_name='Check-in date'),
        ),
        migrations.AlterField(
            model_name='location',
            name='check_out',
            field=models.DateTimeField(default='2023-12-22', verbose_name='Check-out date'),
        ),
    ]