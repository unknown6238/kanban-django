# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-15 14:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_auto_20160514_0311'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='owner',
        ),
    ]
