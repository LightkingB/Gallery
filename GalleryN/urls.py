"""GalleryN URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from GalleryN import settings
from portfolio.views import HomeLView, GalleryView, GalleryDetail

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^/$', HomeLView.as_view(), name='HomeLView'),
    url(r'^gallery/$', GalleryView.as_view(), name='GalleryView'),
    url(r'^gallery/(?P<slug>[-\w]+)/$', GalleryDetail.as_view(), name='detail_gallery'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
