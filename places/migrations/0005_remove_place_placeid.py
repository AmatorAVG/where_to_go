# Generated by Django 3.2.5 on 2021-08-01 02:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0004_place_placeid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='placeId',
        ),
    ]
