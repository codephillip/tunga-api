# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-29 11:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tunga_tasks', '0086_auto_20170427_0855'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='progressevent',
            unique_together=set([]),
        ),
    ]
