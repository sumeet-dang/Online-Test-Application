# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-19 21:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestApp', '0009_auto_20170420_0230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='questionImages'),
        ),
    ]
