from django.conf.urls import url
from django.contrib import admin
from news.views import home, NewsListView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home),
]
