# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-11 18:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tunga_profiles', '0026_connection_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='tax_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='tax_percentage',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
