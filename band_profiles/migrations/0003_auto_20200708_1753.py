# Generated by Django 3.0.8 on 2020-07-08 21:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('band_profiles', '0002_auto_20200708_1750'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bandprofile',
            old_name='text1',
            new_name='bandName',
        ),
        migrations.RenameField(
            model_name='bandprofile',
            old_name='text2',
            new_name='bandSummary',
        ),
    ]
