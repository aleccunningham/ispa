# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-06 05:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20170805_1711'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='owners',
        ),
        migrations.AddField(
            model_name='attendance',
            name='is_owner',
            field=models.BooleanField(default=False),
        ),
    ]
