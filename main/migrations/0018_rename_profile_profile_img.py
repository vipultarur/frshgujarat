# Generated by Django 3.2.11 on 2024-03-05 10:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_profile_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='profile',
            new_name='img',
        ),
    ]
