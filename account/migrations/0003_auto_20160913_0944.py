# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-13 09:44
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20160913_0759'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='created_data',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='created_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
