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


class MainListView(ListView):
    queryset = SingleNews.objects.all()
    template_name = 'index.html'


class ChildListView(ListView):
    queryset = SingleNews.objects.all().filter(category__iexact=u"Дети")
    template_name = 'childs.html'


class ThingsListView(ListView):
    queryset = SingleNews.objects.all().filter(category__iexact=u"Вещи")
    template_name = 'things.html'


class HobbyListView(ListView):
    queryset = SingleNews.objects.all().filter(category__iexact=u"Досуг")
    template_name = 'hobby.html'


class TravelListView(ListView):
    queryset = SingleNews.objects.all().filter(category__iexact=u"Путешествия")
    template_name = 'travel.html'
