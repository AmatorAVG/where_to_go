# Generated by Django 3.2.5 on 2021-07-11 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='title',
            field=models.CharField(default='fff', max_length=255),
            preserve_default=False,
        ),
    ]
