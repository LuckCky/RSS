# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-02 21:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lrss', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='link',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
