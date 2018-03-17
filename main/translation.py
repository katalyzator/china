# -*- coding: utf-8 -*-
from modeltranslation.translator import TranslationOptions, translator

from main.models import *


class BannerTranslationOptions(TranslationOptions):
    fields = ('title',)


class ServiceTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


class StatusTranslationOptions(TranslationOptions):
    fields = ('name',)


class MembersTranslationOptions(TranslationOptions):
    fields = ('name', 'short_description')


class NewsTranslationOptions(TranslationOptions):
    fields = ('short_description', 'description')


class AboutUsTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


class InformationTranslationOptions(TranslationOptions):
    fields = ('title',)


class TitleInfoTranslationOptions(TranslationOptions):
    fields = ('type',)


class ContactsTranslateOptions(TranslationOptions):
    fields = ('name', 'comment')


translator.register(Banner, BannerTranslationOptions)
translator.register(Service, ServiceTranslationOptions)
translator.register(Status, StatusTranslationOptions)
translator.register(Members, MembersTranslationOptions)
translator.register(News, NewsTranslationOptions)
translator.register(AboutUs, AboutUsTranslationOptions)
translator.register(InformationTitle, TitleInfoTranslationOptions)
translator.register(Information, InformationTranslationOptions)
translator.register(Contacts, ContactsTranslateOptions)
