# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-04 15:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user_data',
            fields=[
                ('user', models.CharField(max_length=120, primary_key=True, serialize=False)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('village', models.CharField(blank=True, max_length=120, null=True)),
                ('email', models.CharField(blank=True, max_length=120, null=True)),
                ('Desi', models.CharField(blank=True, max_length=100, null=True)),
                ('PO', models.CharField(blank=True, max_length=100, null=True)),
                ('Mobile', models.DecimalField(decimal_places=0, max_digits=10)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('state', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
