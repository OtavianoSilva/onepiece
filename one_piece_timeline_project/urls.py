
from django.contrib import admin
from django.urls import path, include
from core.views.site import MangaTimeLineView, AnimeTimeLineView
# import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("core.urls"))
]
handler404 = 'core.views.site.error_404'

# urlpatterns+= static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
