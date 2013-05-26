from django.conf.urls import patterns, include, url
import views
from DjangoTemplate.views import current_datetime, current_datetime_t_split,\
    current_datetime_simple, current_datetime_sub1, current_datetime_sub2

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'DjangoHelloworld.views.home', name='home'),
    # url(r'^DjangoHelloworld/', include('DjangoHelloworld.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    ('^time/$', current_datetime_simple),
    ('^time1/$', current_datetime_sub1),
    ('^time2/$', current_datetime_sub2),
     #url(r'^admin/', include(admin.site.urls))
)
#urlpatterns = patterns('',
#    ('^time/$', current_datetime),
#)
