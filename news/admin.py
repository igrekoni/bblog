from django.contrib import admin
from .models import SingleNews


class NewsAdmin(admin.ModelAdmin):
    list_display = ["__unicode__", "updated", "timestamp", "category"]
    list_display_links = ["__unicode__", "category"]
    list_filter = ["updated", "timestamp"]
    search_fields = ["__unicode__", "fullText"]

    class Meta:
        model = SingleNews


admin.site.register(SingleNews, NewsAdmin)
