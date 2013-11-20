from django.conf.urls import patterns, include, url
from django_u4.core.views import FooListView

urlpatterns = patterns('',
    url(r'^list/$', FooListView.as_view()),
)
