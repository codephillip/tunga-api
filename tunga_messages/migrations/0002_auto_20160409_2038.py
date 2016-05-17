# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-09 20:38
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tunga_messages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reception',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.SmallIntegerField(choices=[(1, 'New'), (2, 'Read'), (3, 'Deleted')], default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('read_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='recipient',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='recipient',
            name='message',
        ),
        migrations.RemoveField(
            model_name='recipient',
            name='user',
        ),
        migrations.AlterField(
            model_name='message',
            name='recipients',
            field=models.ManyToManyField(blank=True, related_name='messages_received', through='tunga_messages.Reception', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Recipient',
        ),
        migrations.AddField(
            model_name='reception',
            name='message',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tunga_messages.Message'),
        ),
        migrations.AddField(
            model_name='reception',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='reception',
            unique_together=set([('user', 'message')]),
        ),
    ]