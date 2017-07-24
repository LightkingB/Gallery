# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.validators import slug_re
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView

from portfolio.models import Subscribe, Gallery, Category


class HomeLView(ListView):
    model = Subscribe
    template_name = 'index.html'


def about(request):
    return render(request, "about.html", {})


def contact(request):
    return render(request, "contact.html", {})


# class AboutView(ListView):
#     template_name = 'about.html'
#
#
# class ContactView(ListView):
#     template_name = 'contact.html'


class GalleryView(ListView):
    model = Gallery
    template_name = 'gallery.html'

    def get_context_data(self, **kwargs):
        context = super(GalleryView, self).get_context_data(**kwargs)

        context['gallery'] = Gallery.objects.all()
        context['category'] = Category.objects.all()

        return context


class GalleryDetail(DetailView):
    model = Gallery
    template_name = "gallery_detail.html"
    context_object_name = 'gallery'

    def get_object(self, queryset=None):
        return get_object_or_404(Gallery, slug__iexact=self.kwargs['slug'])
