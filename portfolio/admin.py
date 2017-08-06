# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from transliterate import translit

from portfolio.models import Category, Portfolio, Slider, Result, Services, ServicesCategory


class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('title', 'publish', 'category')
    list_filter = ('title', 'publish', 'category')
    filter_horizontal = ('results', 'slider')


def translate_word(word):
    result = (
        str(translit(u"{}".format(word), "ru", reversed=True)).replace(' ', '').replace('\'', '').lower())
    return result


class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('url',)

    def save_model(self, request, obj, form, change):
        obj.url = translate_word(obj.name)
        return obj.save()


class ServicesCategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('filter_by_category',)

    def save_model(self, request, obj, fortm, change):
        val = translate_word(obj.name)
        obj.filter_by_category = "".join(val)
        # print val
        return obj.save()


class ServicesAdmin(admin.ModelAdmin):
    filter_horizontal = ('image',)


admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Slider)
admin.site.register(Result)
admin.site.register(Services, ServicesAdmin)
admin.site.register(ServicesCategory, ServicesCategoryAdmin)
