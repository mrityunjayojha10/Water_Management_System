# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-25 19:46
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wms', '0007_auto_20171025_1824'),
    ]

    operations = [
        migrations.AddField(
            model_name='plant_data',
            name='date_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
