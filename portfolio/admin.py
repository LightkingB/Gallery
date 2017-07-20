# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from portfolio.models import Category, Gallery, Slider, Result


class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'publish', 'category')
    list_filter = ('title', 'publish', 'category')
    filter_horizontal = ('results', 'slider')


admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Category)
admin.site.register(Slider)
admin.site.register(Result)
