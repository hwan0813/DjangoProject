# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-10 06:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crawl', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogdata',
            name='link',
            field=models.CharField(max_length=300),
        ),
    ]
