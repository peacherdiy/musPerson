from django.conf.urls import *
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^admin/(.*)', admin.site.get_urls()),
    url(r'^', admin.site.get_urls()),
)
