# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
from django.core import serializers
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse

from main.forms import ContactForm
from django.http import JsonResponse
from django.shortcuts import render, render_to_response
from main.models import *


# Create your views here.
def info(request):
    infotitle = InformationTitle.objects.all()

    params = {
        'type': infotitle,
    }
    return render(request, 'app/misc/info.html', params)


def index(request):
    request.session['page_id'] = 1
    banner = Banner.objects.all()
    about_us = AboutUs.objects.all()[:1]
    members = Members.objects.all()
    paginator = Paginator(News.objects.all().order_by('-date'), 8)
    _news = paginator.page(1)
    page_count = paginator.num_pages
    info_title = InformationTitle.objects.all()
    service = Service.objects.order_by('id')
    contact_form = ContactForm(request.POST)
    slider = Slider.objects.order_by('id')
    post = Emails.objects.all()
    number = Phones.objects.all()

    params = {
        'banner': banner,
        'about_us': about_us,
        'members': members,
        'news': _news,
        'page_count': page_count,
        'type': info_title,
        'service': service,
        'form': contact_form,
        'slider': slider,
        'post': post,
        'number': number,

    }
    return render(request, 'app/index.html', params)


def service_modal(request, id):
    service = Service.objects.get(id=id)
    return render_to_response(request, {'service': service})


def news_modal(request, id):
    news = News.objects.get(id=id)
    return render_to_response(request, {'news': news})


def ajax_get_news(request):
    paginator = Paginator(News.objects.all().order_by('-date'), 8)
    _news = paginator.page(request.GET.get('page', 1))
    return render_to_response('app/misc/news_paginate.html', {'news': _news})


def sertificate(request):
    slider = Slider.objects.get(id=id)

    params = {
        'slider': slider,
    }
    return render(request, 'app/misc/sertificate.html', params)


def contacts(request):
    post = Emails.objects.all()
    number = Phones.objects.all()

    params = {
        'post': post,
        'number': number,
    }
    return render(request, 'app/misc/mail.html', params)


def feedback(request):
    contact_form = ContactForm(request.POST)
    if request.POST:
        print "NotError"
        if contact_form.is_valid():
            print "NotError"
            c = Contacts()
            c.name = contact_form.cleaned_data['name']
            c.email = contact_form.cleaned_data['email']
            c.phone = contact_form.cleaned_data['phone']
            c.comment = contact_form.cleaned_data['comment']
            c.save()
            return JsonResponse(dict(success=True, message='Успешно!!'))
        return JsonResponse(dict(success=False, message='Форма не валидна'))
