
from django.contrib import admin
from django.urls import path
from core.views import ArcView
# import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", ArcView.as_view()),
]

# urlpatterns+= static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
