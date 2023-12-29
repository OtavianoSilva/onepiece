
from django.contrib import admin
from django.urls import path, include
from .views.site import MangaTimeLineView, AnimeTimeLineView
from .views.api import chapter_overview, chapter_detail
# import settings

urlpatterns = [
    # Mangá
    path(
            "",
            MangaTimeLineView.as_view(),
        ),
    path(
            "manga",
            MangaTimeLineView.as_view(),
            name="manga",
        ),
    path(
            "manga/<slug:slug>",
            MangaTimeLineView.as_view(),
            name="manga/search",
        ),

    # Anime
    path(
            "anime",
            AnimeTimeLineView.as_view(),
            name="anime",
        ),
    path(
            "anime/nofillers",
            AnimeTimeLineView.nofiller,
            name="anime/nofillers",
        ),
    path(
            "anime/<slug:slug>",
            AnimeTimeLineView.as_view(),
            name="anime/search",
        ),

    # Api
    path(
        "api/chapter/overview/",
        chapter_overview,
        name="chapter overview",
    ),
    path(
        "api/chapter/<int:pk>/",
        chapter_detail,
        name="chapter detail",
    ),
]