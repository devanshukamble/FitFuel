# Generated by Django 5.0.6 on 2024-06-29 13:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_remove_userprofile_activity_level_userprofile_veg_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='email',
        ),
    ]
