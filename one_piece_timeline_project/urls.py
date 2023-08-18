
from django.contrib import admin
from django.urls import path
from core.views import MangaTimeLineView, AnimeTimeLineView
# import settings

urlpatterns = [
    path("admin/", admin.site.urls),

    path("", MangaTimeLineView.as_view()),
    path("manga", MangaTimeLineView.as_view(), name="manga"),
    path("manga/year/<slug:slug>/", MangaTimeLineView.search_year, name="manga/year"),
    path("manga/saga/<slug:slug>", MangaTimeLineView.search_saga, name="manga/saga"),
    
    path("anime", AnimeTimeLineView.as_view(), name="anime"),
    path("anime/nofillers", AnimeTimeLineView.nofiller, name="anime/nofillers"),
    path("anime/year/<slug:slug>", AnimeTimeLineView.search_year, name="anime/year"),
    path("anime/saga/<slug:slug>", AnimeTimeLineView.search_saga, name="anime/saga"),
]
handler404 = 'core.views.error_404'

# urlpatterns+= static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
