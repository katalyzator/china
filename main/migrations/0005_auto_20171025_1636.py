# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-10-25 10:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20171025_1629'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='information',
            options={'verbose_name': '\u041f\u043e\u043b\u0435\u0437\u043d\u0443\u044e \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044e', 'verbose_name_plural': '\u041f\u043e\u043b\u0435\u0437\u043d\u044b\u0435 \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u0438'},
        ),
        migrations.AlterField(
            model_name='information',
            name='link',
            field=models.URLField(verbose_name='\u0421\u0441\u044b\u043b\u043a\u0430'),
        ),
        migrations.AlterField(
            model_name='information',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, verbose_name='\u041d\u043e\u043c\u0435\u0440 \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0430'),
        ),
        migrations.AlterField(
            model_name='information',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='type_info', to='main.InformationTitle'),
        ),
        migrations.AlterField(
            model_name='informationtitle',
            name='title',
            field=models.CharField(max_length=155, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u0438'),
        ),
        migrations.AlterField(
            model_name='informationtitle',
            name='title_ch',
            field=models.CharField(max_length=155, null=True, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u0438'),
        ),
        migrations.AlterField(
            model_name='informationtitle',
            name='title_en',
            field=models.CharField(max_length=155, null=True, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u0438'),
        ),
        migrations.AlterField(
            model_name='informationtitle',
            name='title_ru',
            field=models.CharField(max_length=155, null=True, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u0438'),
        ),
        migrations.AlterModelTable(
            name='information',
            table='information',
        ),
    ]
