# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-02 22:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20170802_2135'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='slug',
            field=models.SlugField(blank=True, max_length=40, null=True, unique=True),
        ),
    ]
