from django.conf import settings
from django.conf.urls.static import static
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


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
