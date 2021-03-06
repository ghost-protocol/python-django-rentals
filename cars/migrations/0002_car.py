# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-05 14:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('manufacturer', models.CharField(max_length=200)),
                ('engine', models.CharField(max_length=20)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.Cartype')),
            ],
        ),
    ]
