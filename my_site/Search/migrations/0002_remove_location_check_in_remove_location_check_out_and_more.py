# Generated by Django 4.1.4 on 2022-12-19 22:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Search', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='check_in',
        ),
        migrations.RemoveField(
            model_name='location',
            name='check_out',
        ),
        migrations.RemoveField(
            model_name='location',
            name='guests_number',
        ),
    ]
