# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline, TabbedTranslationAdmin

from models import *


# Register your models here.

class BannerAdmin(TabbedTranslationAdmin):
    list_display = ["title_ru", "title_ch"]


class ServiceAdmin(TabbedTranslationAdmin):
    list_display = ["title_ru", "title_ch", 'description_ru', 'description_ch']


class StatusAdmin(TabbedTranslationAdmin):
    list_display = ["name_ru", 'name_ch']


class MembersAdmin(TabbedTranslationAdmin):
    list_display = ["name_ru", 'name_ch', 'short_description_ru', 'short_description_ch']


class NewsAdmin(TabbedTranslationAdmin):
    list_display = ['short_description_ru', 'short_description_ch', 'description_ru', 'description_ch']


class InformationAdmin(TabbedTranslationAdmin):
    list_display = ["title_ru", "title_ch", ]


class ContactsAdmin(TabbedTranslationAdmin):
    list_display = ["name_ru", 'name_ch', 'comment_ru', 'comment_ch']


class AboutUsAdmin(TabbedTranslationAdmin):
    list_display = ["title_ru", "title_ch", 'description_ru', 'description_ch']


class PhonesAdmin(admin.ModelAdmin):
    list_display = ["phone"]
    # list_editable = ["phone"]


class EmailsAdmin(admin.ModelAdmin):
    list_display = ["email"]
    # list_editable = ["email"]


class InformationTitleAdmin(admin.ModelAdmin):
    list_display = ["type_ru", "type_ch",]


admin.site.register(Banner, BannerAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(Members, MembersAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(InformationTitle, InformationTitleAdmin)
admin.site.register(Information, InformationAdmin)
admin.site.register(Contacts, ContactsAdmin)
admin.site.register(AboutUs, AboutUsAdmin)
admin.site.register(Slider, )
admin.site.register(Phones, PhonesAdmin)
admin.site.register(Emails, EmailsAdmin)
