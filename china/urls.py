"""china URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from solid_i18n.urls import solid_i18n_patterns
from china import settings
from main.views import *

urlpatterns = solid_i18n_patterns(
    url(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^$', index, name='index'),
    url(r'^feedback/$', feedback, name='feedback'),
    url(r'^news/get$', ajax_get_news, name='news_paginate'),
    # url(r'^load_news/$', load_news, name='load_news'),
    # url(r'^contacts/$', contacts, name='contacts'),
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
