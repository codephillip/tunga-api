# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-24 10:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tunga_messages', '0008_auto_20160626_1756'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='reception',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='reception',
            name='message',
        ),
        migrations.RemoveField(
            model_name='reception',
            name='user',
        ),
        migrations.RemoveField(
            model_name='reply',
            name='message',
        ),
        migrations.RemoveField(
            model_name='reply',
            name='user',
        ),
        migrations.RemoveField(
            model_name='message',
            name='is_broadcast',
        ),
        migrations.RemoveField(
            model_name='message',
            name='read_at',
        ),
        migrations.RemoveField(
            model_name='message',
            name='recipients',
        ),
        migrations.RemoveField(
            model_name='message',
            name='subject',
        ),
        migrations.DeleteModel(
            name='Reception',
        ),
        migrations.DeleteModel(
            name='Reply',
        ),
    ]
