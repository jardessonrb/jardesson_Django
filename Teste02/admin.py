# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Contato


class ContatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone')


admin.site.register(Contato, ContatoAdmin)