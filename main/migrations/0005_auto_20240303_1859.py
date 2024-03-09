# Generated by Django 3.2.11 on 2024-03-03 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20240303_1641'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('des', models.CharField(max_length=100, unique=True)),
                ('status', models.BooleanField(default=False)),
                ('img', models.ImageField(default='', upload_to='Banner/img')),
            ],
        ),
        migrations.AlterField(
            model_name='classcis',
            name='img',
            field=models.ImageField(default='', upload_to='Classcis/'),
        ),
    ]
