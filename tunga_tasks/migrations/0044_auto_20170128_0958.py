# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-01-28 09:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tunga_tasks', '0043_auto_20170124_0655'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='timeentry',
            options={'ordering': ['spent_at']},
        ),
        migrations.AlterField(
            model_name='task',
            name='fee',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=19, null=True),
        ),
    ]
