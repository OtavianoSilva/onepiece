from django.contrib import admin
from .models import *

class ArcAdmin(admin.ModelAdmin):
    list_display = ["name", "background_color", "background_shadow"]
class ChapterAdmin(admin.ModelAdmin):
    list_display = ["number", "title", "year", "arc"]


admin.site.register(Arc, ArcAdmin)
admin.site.register(Chapter, ChapterAdmin)