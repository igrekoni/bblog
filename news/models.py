from django.conf import settings
from django.db import models


class SingleNews(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)
    title = models.CharField(max_length=120, blank=False)
    previewText = models.TextField(max_length=260, blank=True)
    fullText = models.TextField()
    publish = models.DateField(auto_now=False, auto_now_add=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    slug = models.SlugField(unique=True)
    category = models.CharField(max_length=40, default='Common')

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title
