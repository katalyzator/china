# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ckeditor_uploader.fields import RichTextUploadingField
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import ugettext_lazy as _
from sorl.thumbnail import ImageField
from django.db import models

# Create your models here.
from china.media_path import *


class Phones(models.Model):
    phone = models.CharField(verbose_name='Номер телефона', max_length=100)

    def __unicode__(self):
        return self.phone

    class Meta:
        db_table = 'Phones'
        verbose_name = 'Номер телефона'
        verbose_name_plural = 'Номера телефонов'


class Emails(models.Model):
    email = models.EmailField(verbose_name='Email адрес')

    def __unicode__(self):
        return self.email

    class Meta:
        db_table = 'Emails'
        verbose_name = 'Электронный адрес'
        verbose_name_plural = 'Электронные адреса'


class Banner(models.Model):
    title = models.CharField(max_length=100, blank=True, verbose_name=_('Описание'))
    image = models.ImageField(upload_to=banner_path, verbose_name=_('Изображение'))

    def __unicode__(self):
        return self.title

    class Meta:
        db_table = 'banner'
        verbose_name = _('Баннер')
        verbose_name_plural = _('Баннеры')


class Service(models.Model):
    title = models.CharField(max_length=100, verbose_name=_('Название'))
    description = RichTextUploadingField(verbose_name=_('Описание'))
    icon = models.ImageField(upload_to=service_path, verbose_name=_('иконка'))
    image = models.ImageField(upload_to=service_path, verbose_name=_('Изображение'))
    link = models.URLField(verbose_name=_('Cсылка'), blank=True, null=True)

    def __unicode__(self):
        return self.title

    class Meta:
        db_table = 'service'
        verbose_name = _('услугу')
        verbose_name_plural = _('услуги')


class Status(models.Model):
    name = models.CharField(max_length=150, verbose_name=_('Статус'))

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _('Статус')
        verbose_name_plural = _('Статусы')


class Members(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('Имя'))
    status = models.ForeignKey(Status, related_name=_('status_members'))
    short_description = RichTextUploadingField(max_length=255, verbose_name=_('Краткое описание'))
    image = models.ImageField(upload_to=members_path, verbose_name=_('Изображение'))

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'members'
        verbose_name = _('партнера')
        verbose_name_plural = _('команда')


class News(models.Model):
    short_description = models.CharField(max_length=255, verbose_name=_('Краткое описание'))
    description = RichTextUploadingField(blank=True, null=True, verbose_name=_('Описание'))
    image = ImageField(upload_to=news_path, verbose_name=_('Изображение'))
    date = models.DateTimeField(auto_now_add=True, verbose_name=_('Дата'))
    link = models.URLField(verbose_name=_('ссылка'), blank=True, null=True)

    def __unicode__(self):
        return str(self.date)

    class Meta:
        db_table = 'news'
        verbose_name = _('новость')
        verbose_name_plural = _('новости')


class Slider(models.Model):
    # title = models.CharField(max_length=100, default='')
    image = models.ImageField(upload_to=slider_path, verbose_name=_('Изображение'))

    def __unicode__(self):
        return self.image.url

    class Meta:
        db_table = 'sliders'
        verbose_name = _('Сертификат')
        verbose_name_plural = _('Сертификаты')


class AboutUs(models.Model):
    title = models.CharField(max_length=30, verbose_name=_('Название'))
    description = RichTextUploadingField(verbose_name=_('Описание'))

    def __unicode__(self):
        return self.title

    class Meta:
        db_table = 'about_us'
        verbose_name = _('о нас')
        verbose_name_plural = _('о нас')


class Contacts(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('Имя'))
    email = models.EmailField(verbose_name=_('E-mail'))
    phone = PhoneNumberField(blank=True, null=True, verbose_name=_('НОмер телефона'))
    comment = RichTextUploadingField()
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'contacts'
        verbose_name = _('контакт')
        verbose_name_plural = _('контакты')


class InformationTitle(models.Model):
    type = models.CharField(max_length=155, verbose_name=_('Название'))
    steps = models.ManyToManyField('Information', verbose_name=_('Информацию'))

    def __unicode__(self):
        return self.type

    class Meta:
        db_table = 'information_title'
        verbose_name = _('Полезную информацию')
        verbose_name_plural = _('Полезная информация')


class Information(models.Model):
    title = models.CharField(max_length=155, verbose_name=_('Название'))
    phone = models.CharField(max_length=100, verbose_name='Номер телефона', blank=True, null=True)
    link = models.URLField(verbose_name='Ссылка', blank=True, null=True)

    # type = models.ForeignKey(InformationTitle, related_name=_('type_info'), verbose_name=_('Заголовок информации'))

    def __unicode__(self):
        return self.title

    class Meta:
        db_table = 'information'
        verbose_name = _('Информацию')
        verbose_name_plural = _('Информации')
