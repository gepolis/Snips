from django.contrib import admin
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
