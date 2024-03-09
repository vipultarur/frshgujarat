# Generated by Django 3.2.11 on 2024-03-03 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20240303_1456'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classcis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('price', models.IntegerField(default='')),
                ('dec', models.CharField(max_length=300)),
                ('status', models.BooleanField(default=False)),
                ('img', models.ImageField(default='', upload_to='Banner/img')),
            ],
        ),
    ]
