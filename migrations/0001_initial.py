# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-15 14:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SearchQuery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('query', models.CharField(max_length=100)),
                ('search_time', models.DateTimeField(verbose_name='time searched')),
            ],
        ),
    ]
