# coding=utf-8
from __future__ import unicode_literals
from django import forms
from main.models import Contacts


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = ['name', 'email', 'phone', 'comment']
