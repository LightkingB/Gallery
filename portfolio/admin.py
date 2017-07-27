# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import cyrtranslit
from django.contrib import admin
from django.utils.text import slugify
from transliterate import translit

from portfolio.models import Category, Portfolio, Slider, Result


class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('title', 'publish', 'category')
    list_filter = ('title', 'publish', 'category')
    filter_horizontal = ('results', 'slider')


class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('url',)

    def save_model(self, request, obj, form, change):
        obj.url = (str(translit(u"{}".format(obj.name), "ru", reversed=True)).replace(' ', '').lower())
        return obj.save()


admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Slider)
admin.site.register(Result)
