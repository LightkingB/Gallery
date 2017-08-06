# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView

from portfolio.models import Subscribe, Portfolio, Category, Services


class HomeLView(ListView):
    model = Subscribe
    template_name = 'index.html'


def about(request):
    return render(request, "about.html", {})


def contact(request):
    return render(request, "contact.html", {})


def client(request):
    return render(request, "client.html", {})


class PortfolioView(ListView):
    model = Portfolio
    template_name = 'portfolio.html'

    def get_context_data(self, **kwargs):
        context = super(PortfolioView, self).get_context_data(**kwargs)

        context['portfolio'] = Portfolio.objects.all()
        context['category'] = Category.objects.all()

        return context


class PortfolioDetail(DetailView):
    model = Portfolio
    template_name = "portfolio_detail.html"
    context_object_name = 'gallery'

    def get_object(self, queryset=None):
        return get_object_or_404(Portfolio, slug__iexact=self.kwargs['slug'])


class ServicesView(ListView):
    model = Services
    template_name = "services.html"

    def get_context_data(self, **kwargs):
        context = super(ServicesView, self).get_context_data(**kwargs)
        category = self.kwargs['category']
        status = False

        if category == "graficheskijdizajnnaruzhnajareklama":
            status = True
        context['services'] = get_object_or_404(Services,
                                                categ_service__filter_by_category__iexact=category)
        context['status'] = status
        return context
