# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-07-10 21:15
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SHOWS', '0003_shows_release_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shows',
            name='release_date',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]