# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-04 23:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='report',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='report',
            name='rel_reports',
        ),
    ]
