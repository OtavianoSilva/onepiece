from django.contrib import admin
from .models import *

class SagaAdmin(admin.ModelAdmin):
    list_display = ["name"]

class ArcAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "filler", "saga", "text_color", "background_color", "background_shadow"]

class ChapterAdmin(admin.ModelAdmin):
    list_display = ["number", "title", "year", "arc", "spoiler"]

class EpisodeAdmin(admin.ModelAdmin):
    list_display = ["number", "title", "year", "arc", "filler"]

admin.site.register(Saga, SagaAdmin)
admin.site.register(Arc, ArcAdmin)
admin.site.register(Chapter, ChapterAdmin)
admin.site.register(Episode, EpisodeAdmin)