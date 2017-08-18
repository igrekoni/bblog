from django.conf.urls import url
from django.contrib import admin
from news.views import (
    MainListView,
    ChildListView,
    ThingsListView,
    HobbyListView,
    TravelListView
)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^childs/$', ChildListView.as_view()),
    url(r'^things/$', ThingsListView.as_view()),
    url(r'^hobby/$', HobbyListView.as_view()),
    url(r'^travel/$', TravelListView.as_view()),
    url(r'^$', MainListView.as_view()),
]
