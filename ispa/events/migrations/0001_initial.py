# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-04 23:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('did_attend', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(blank=True, max_length=40, null=True, unique=True)),
                ('date', models.DateTimeField(blank=True, null=True, verbose_name='Event Date')),
                ('description', models.CharField(blank=True, max_length=512, null=True, verbose_name='Description')),
                ('is_active', models.BooleanField(default=True)),
                ('name', models.CharField(blank=True, max_length=256, null=True, verbose_name='Name')),
                ('points', models.IntegerField()),
                ('event_type', models.CharField(blank=True, choices=[(8, 'event'), (5, 'semester'), (3, 'meeting')], max_length=128, null=True, verbose_name='Event Type')),
                ('guests', models.ManyToManyField(through='events.Attendance', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='EventLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('address', models.CharField(blank=True, max_length=45, null=True, verbose_name='Address')),
                ('address2', models.CharField(blank=True, max_length=45, null=True, verbose_name='Address 2')),
                ('city', models.CharField(blank=True, max_length=45, null=True, verbose_name='City')),
                ('state', models.CharField(blank=True, max_length=45, null=True, verbose_name='State')),
                ('zipcode', models.CharField(blank=True, max_length=10, null=True, verbose_name='Zipcode')),
            ],
            options={
                'abstract': False,
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Event')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.EventLocation'),
        ),
        migrations.AddField(
            model_name='event',
            name='owners',
            field=models.ManyToManyField(related_name='owners', through='events.Owner', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='attendance',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attendees', to='events.Event'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to=settings.AUTH_USER_MODEL),
        ),
    ]
