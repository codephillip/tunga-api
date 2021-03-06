# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-10 10:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tunga_utils.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tunga_tasks', '0090_task_hubspot_deal_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='MultiTaskPayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('btc_address', models.CharField(max_length=40, validators=[tunga_utils.validators.validate_btc_address])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
        migrations.AlterField(
            model_name='task',
            name='hubspot_deal_id',
            field=models.CharField(editable=False, max_length=12, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='multi_task_payment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='multi_tasks', to='tunga_tasks.MultiTaskPayment'),
        ),
    ]
