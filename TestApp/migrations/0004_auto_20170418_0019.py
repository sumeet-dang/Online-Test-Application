# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-17 18:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TestApp', '0003_auto_20170417_0300'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Student',
            new_name='Candidate',
        ),
    ]
