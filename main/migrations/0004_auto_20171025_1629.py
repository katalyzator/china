# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-10-25 10:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_information'),
    ]

    operations = [
        migrations.AddField(
            model_name='information',
            name='title_ch',
            field=models.CharField(max_length=155, null=True),
        ),
        migrations.AddField(
            model_name='information',
            name='title_en',
            field=models.CharField(max_length=155, null=True),
        ),
        migrations.AddField(
            model_name='information',
            name='title_ru',
            field=models.CharField(max_length=155, null=True),
        ),
        migrations.AddField(
            model_name='informationtitle',
            name='title_ch',
            field=models.CharField(max_length=155, null=True),
        ),
        migrations.AddField(
            model_name='informationtitle',
            name='title_en',
            field=models.CharField(max_length=155, null=True),
        ),
        migrations.AddField(
            model_name='informationtitle',
            name='title_ru',
            field=models.CharField(max_length=155, null=True),
        ),
    ]
