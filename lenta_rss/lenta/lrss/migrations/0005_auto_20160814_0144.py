# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-13 22:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lrss', '0004_auto_20160814_0138'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='name',
            new_name='title',
        ),
    ]
