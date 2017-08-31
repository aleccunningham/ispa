# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-28 23:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    def events_are_active(apps, schema_editor):
        EventLocation = apps.get_model("events", "EventLocation")
        locations = EventLocation.objects.all()

        print("Updating locations to active")
        for location in locations:
            location.is_active = True
            location.save()

    dependencies = [
        ('events', '0022_eventlocation_is_active'),
    ]

    operations = [
        migrations.RunPython(events_are_active)
    ]