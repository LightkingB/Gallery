# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import random
import string
from datetime import datetime

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Category(models.Model):
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    name = models.CharField(max_length=100)
    url = models.CharField(max_length=100, null=True, blank=True)

    def __unicode__(self):
        return self.name


def generate_random_string(digit_length=6, char_length=6):
    digits = "".join([random.choice(string.digits) for i in xrange(6)])
    chars = "".join([random.choice(string.letters) for i in xrange(6)])
    return digits + chars


def item_upload_to(instance, filename):
    file_root, file_ext = os.path.splitext(filename)
    date = datetime.now().strftime("%Y/%m/%d")
    random_name = generate_random_string() + file_ext

    return '/'.join(['gallery-media', date, random_name])


def img_upload_to_slider(instance, filename):
    file_root, file_ext = os.path.splitext(filename)
    date = datetime.now().strftime("%Y/%m/%d")
    random_name = generate_random_string() + file_ext

    return '/'.join(['slider-media', date, random_name])


class Slider(models.Model):
    class Meta:
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайды'

    title = models.CharField(max_length=255, null=True, blank=True)
    slide = models.ImageField(upload_to=img_upload_to_slider)

    def __unicode__(self):
        return self.title


class Result(models.Model):
    class Meta:
        verbose_name = 'Результат'
        verbose_name_plural = 'Результаты'

    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class Gallery(models.Model):
    class Meta:
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галерея'

    title = models.CharField(max_length=150)
    publish = models.DateTimeField(auto_now_add=True)
    video = models.CharField(max_length=255, null=True, blank=True)
    link = models.CharField(max_length=255, null=True, blank=True)
    results = models.ManyToManyField(Result)
    place = models.CharField(max_length=60)
    description = models.TextField()
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to=item_upload_to)
    category = models.ForeignKey(Category)
    slider = models.ManyToManyField(Slider)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail_gallery', args=[str(self.slug)])


class Subscribe(models.Model):
    class Meta:
        verbose_name = 'Подписчик'
        verbose_name_plural = 'Подписчики'

    email = models.EmailField(max_length=100)

    def __unicode__(self):
        return self.email

# slug field - add data by form

# def create_slug(instance, new_slug=None):
#     slug = slugify(instance.title)
#     if new_slug is not None:
#         slug = new_slug
#     qs = Gallery.objects.filter(slug=slug)
#     exists = qs.exists()
#     if exists:
#         new_slug = "%s-%s" % (slug, qs.first().id)
#         return create_slug(instance, new_slug=new_slug)
#     return slug
#
#
# def pre_save_post_signal_receiver(sender, instance, *args, **kwargs):
#     if not instance.slug:
#         instance.slug = create_slug(instance)
#
#
# pre_save.connect(pre_save_post_signal_receiver, sender=Gallery)
