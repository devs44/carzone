# Generated by Django 3.0.7 on 2021-03-01 17:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_title', models.CharField(max_length=255)),
                ('state', models.CharField(choices=[('Ktm', 'Kathmandu'), ('Ptn', 'Patan'), ('Lp', 'Lalitpur'), ('Bhkt', 'Bhaltapur'), ('Rmchp', 'Rammechhap')], max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('description', models.CharField(max_length=200)),
                ('car_photo_1', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('car_photo_2', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('car_photo_3', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('car_photo_4', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('is_featured', models.BooleanField(max_length=100)),
                ('created_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]