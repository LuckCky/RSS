# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-13 22:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lrss', '0003_auto_20160814_0136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='date',
            field=models.DateField(verbose_name='date published'),
        ),
    ]
