# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-21 22:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestApp', '0013_testschedule'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testschedule',
            name='test_date',
        ),
        migrations.AddField(
            model_name='testschedule',
            name='is_open',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='testschedule',
            name='subject',
            field=models.CharField(choices=[('Aptitude', 'Aptitude')], default='Aptitude', max_length=20),
            preserve_default=False,
        ),
    ]
