# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-05 14:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_auto_20170305_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.Cartype'),
        ),
    ]