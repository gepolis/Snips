import random

from django.contrib import admin
from django.db.models import QuerySet

from MainApp.models import *

# Register your models here.


@admin.register(Languages)
class LanguageModelAdmin(admin.ModelAdmin):
    list_display = ("id", "language", "show")
    list_filter = ("show",)


@admin.register(Snippet)
class SnippetModelAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "language", "creation_date", "author","public")
    list_filter = ('language',"public")
    actions = ['set_public','set_private','set_random']
    search_fields = ["name"]
    readonly_fields = ["author"]
    @admin.action(description="Сделать выделенное публичным")
    def set_public(self, request, qs: QuerySet):
        qs.update(public=True)

    @admin.action(description="Сделать выделенное приватным")
    def set_private(self, request, qs: QuerySet):
        q = qs.update(public=False)
    @admin.action(description="Сделать выделенное публичным илм приватным")
    def set_random(self, request, qs: QuerySet):
        for q in qs.all():
            if random.randint(1,2) == 1: q.public=True
            else: q.public=False
            q.save()
