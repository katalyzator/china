# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-10-25 10:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20171025_1641'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='informationtitle',
            options={'verbose_name': '\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u0438', 'verbose_name_plural': '\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043a\u0438 \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u0439'},
        ),
        migrations.AlterModelTable(
            name='informationtitle',
            table='information_title',
        ),
    ]
