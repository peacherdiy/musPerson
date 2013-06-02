from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('DjangoTemplate.views',
    # Examples:
    # url(r'^$', 'DjangoHelloworld.views.home', name='home'),
    # url(r'^DjangoHelloworld/', include('DjangoHelloworld.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    ('^time/$', 'current_datetime_simple'),
    ('^time1/$', 'current_datetime_sub1'),
    ('^time2/$', 'current_datetime_sub2'),
     url(r'^admin/', include(admin.site.urls))
)

#p103 group URL
urlpatterns += patterns('DjangoTemplate.views',
    (r'^articles/(\d{4})/$', 'year_archive'),
    (r'^articles/(\d{4})/(\d{2})/$', 'month_archive',{'template_name': 'archive_month.html'}),
)

#p103 group URL
urlpatterns += patterns('DjangoTemplate.views',
    (r'^articlesGroupNameYear/(?P<year>\d{4})/$', 'year_archive'),
    (r'^articlesGroupNameMonth/(?P<year>\d{4})/(?P<month>\d{2})/$', 'month_archive'),
)
#urlpatterns = patterns('',
#    ('^time/$', current_datetime),
#)
