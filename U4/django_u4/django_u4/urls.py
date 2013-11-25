from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^foo/', include('django_u4.core.urls')),
    url(r'^simple_view', 'django_u4.views.simple_view'),


    url(r'^admin/', include(admin.site.urls)),
)
