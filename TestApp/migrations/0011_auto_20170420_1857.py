# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-20 13:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TestApp', '0010_auto_20170420_0233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
