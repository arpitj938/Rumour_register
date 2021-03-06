# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-04 08:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='forgot_data',
            fields=[
                ('forgot_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.CharField(blank=True, max_length=120, null=True)),
                ('email', models.CharField(blank=True, max_length=120, null=True)),
                ('otp', models.DecimalField(decimal_places=0, max_digits=6)),
                ('flag', models.SmallIntegerField(default=0)),
            ],
        ),
    ]
