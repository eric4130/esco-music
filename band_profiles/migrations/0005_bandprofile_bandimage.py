# Generated by Django 3.0.8 on 2020-07-21 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('band_profiles', '0004_bandprofile_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='bandprofile',
            name='bandImage',
            field=models.ImageField(default=1, upload_to='images/'),
            preserve_default=False,
        ),
    ]
