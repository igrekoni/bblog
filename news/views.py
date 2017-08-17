from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from .models import SingleNews


def home(request):
    template_name = 'index.html'
    queryset = SingleNews.objects.all()
    context = {
        "object_list": queryset,
    }
    return render(request, template_name, context)


class NewsListView(ListView):
    queryset = SingleNews.objects.all()
    template_name = 'index.html'
