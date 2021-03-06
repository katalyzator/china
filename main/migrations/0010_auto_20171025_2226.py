# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-10-25 16:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20171025_2213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information',
            name='phone',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='\u041d\u043e\u043c\u0435\u0440 \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0430'),
        ),
        migrations.AlterField(
            model_name='information',
            name='title',
            field=models.CharField(max_length=155, verbose_name='\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044e'),
        ),
        migrations.AlterField(
            model_name='information',
            name='title_ch',
            field=models.CharField(max_length=155, null=True, verbose_name='\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044e'),
        ),
        migrations.AlterField(
            model_name='information',
            name='title_en',
            field=models.CharField(max_length=155, null=True, verbose_name='\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044e'),
        ),
        migrations.AlterField(
            model_name='information',
            name='title_ru',
            field=models.CharField(max_length=155, null=True, verbose_name='\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044e'),
        ),
    ]
