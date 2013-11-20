from django.shortcuts import render
from django.views.generic import ListView
from django_u4.core.models import Foo


class FooListView(ListView):
    model = Foo
    #template_name = 'core/foo_list.html'