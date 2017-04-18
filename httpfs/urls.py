"""httpfs URL Configuration

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
from django.conf.urls import include, url
from django.contrib import admin
from httpfs.httpapi import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^get/(?P<filename>[^/]+)$',    views.FileGet.as_view()),
    url(r'^put/(?P<filename>[^/]+)$',    views.FilePut.as_view()),
    url(r'^update/(?P<filename>[^/]+)$', views.FilePut.as_view()),
    url(r'^meta/(?P<filename>[^/]+)$',   views.FileMeta.as_view()),
    url(r'^ls/$',     views.FileList.as_view()),
    url(r'^rm/(?P<filename>[^/]+)$',     views.FileRemove.as_view()),
]

