# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-28 06:21
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wms', '0012_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='contactno',
            field=models.CharField(blank=True, max_length=10, validators=[django.core.validators.MinLengthValidator(10)]),
        ),
    ]
