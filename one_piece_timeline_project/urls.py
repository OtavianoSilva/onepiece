
from django.contrib import admin
from django.urls import path
from core.views import MangaTimeLineView, AnimeTimeLineView
# import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", MangaTimeLineView.as_view()),
    path("manga", MangaTimeLineView.as_view(), name="manga"),
    path("manga/<slug:slug>", MangaTimeLineView.as_view(), name="manga/search"),

    path("anime", AnimeTimeLineView.as_view(), name="anime"),
    path("anime/nofillers", AnimeTimeLineView.nofiller, name="anime/nofillers"),
    path("anime/year/<slug:slug>", AnimeTimeLineView.as_view(), name="anime/search"),
]
handler404 = 'core.views.error_404'

# urlpatterns+= static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
