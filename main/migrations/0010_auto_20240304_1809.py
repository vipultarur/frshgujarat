# Generated by Django 3.2.11 on 2024-03-04 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20240304_1623'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='email',
            field=models.CharField(default=1, max_length=100, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='about',
            name='location',
            field=models.CharField(max_length=100),
        ),
    ]
