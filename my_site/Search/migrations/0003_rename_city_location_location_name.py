# Generated by Django 4.1.4 on 2022-12-19 23:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Search', '0002_remove_location_check_in_remove_location_check_out_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='city',
            new_name='location_name',
        ),
    ]
