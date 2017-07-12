# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-06 14:40
from __future__ import unicode_literals

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('isbn', models.BigIntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=128)),
                ('memo', jsonfield.fields.JSONField(default={})),
            ],
        ),
    ]
