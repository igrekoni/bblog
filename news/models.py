from datetime import timezone

from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save
from unidecode import unidecode
from django.utils import timezone
from django.utils.text import slugify


class PostManager(models.Manager):
    def active(self, *args, **kwargs):
        return super(PostManager, self).filter(draft=False).filter(timezone)


def upload_location(instance, filename):
    return "%s/%s" % (instance.id, filename)


class SingleNews(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)
    title = models.CharField(max_length=120, blank=False)
    previewText = models.TextField(max_length=260, blank=True)
    fullText = models.TextField()
    publish = models.DateField(auto_now=False, auto_now_add=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to=upload_location,
                              null=True, blank=True,
                              height_field='height_field',
                              width_field='width_field')
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    CH = u'Дети'
    TH = u'Вещи'
    DS = u'Досуг'
    TR = u'Путешествия'
    CATEGORY_CHOICES = (
        (CH, u'Дети'),
        (TH, u'Вещи'),
        (DS, u'Досуг'),
        (TR, u'Путешествия'),
    )
    category = models.CharField(max_length=40, choices=CATEGORY_CHOICES, default=CH)
    objects = PostManager()

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title


def create_slug(instance, new_slug=None):
    slug = slugify(unidecode(instance.title))
    if new_slug is not None:
        slug = new_slug
    qs = SingleNews.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

    # if instance.content:
    #     html_string = instance.content
    #     read_time_var = get_read_time(html_string)
    #     instance.read_time = read_time_var


pre_save.connect(pre_save_post_receiver, sender=SingleNews)
