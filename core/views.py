from django.shortcuts import render
from .models import Saga, Arc, Chapter, Episode
from django.views.generic import ListView

class MangaTimeLineView(ListView):
    context = {
        "years": range(1997, 2024),
        "sagas" : Saga.objects.all()
    }

    def get(self, request, slug=None, *args, **kwargs):
        if slug is None:
            self.context["bodycolor"]= "#ffe797"
            self.context["media"] = Chapter.objects.all()
        else:
            if int(slug) in range(1997, 2024):
                self.context["bodycolor"] = "#ff96bd"
                self.context["media"] = Chapter.objects.filter(year=slug)
            else:
                search = Chapter.objects.filter(arc__saga__id=slug)
                if search.count() >= 1:
                    self.context["bodycolor"] = "#cffff1"
                    self.context["media"] = search
                else: return render(request, "404.html")


        return render(request, "manga.html", self.context)

class AnimeTimeLineView(ListView):
    context = {
        "years": range(1999, 2024),
        "sagas" : Saga.objects.all()
    }

    def get(self, request, slug=None, *args, **kwargs):
        if slug is None:
            self.context["bodycolor"]= "#ffe797"
            self.context["media"] = Episode.objects.all()
        else:
            if int(slug) in range(1999, 2024):
                self.context["bodycolor"] = "#ff96bd"
                self.context["media"] = Episode.objects.filter(year=slug)
            else:
                search = Episode.objects.filter(arc__saga__id=slug)
                if search.count() >= 1:
                    self.context["bodycolor"] = "#cffff1"
                    self.context["media"] = search
                else: return render(request, "404.html")

        return render(request, "anime.html", self.context)
    
    def nofiller(request):

        context = {
            "years": range(1999, 2024),
            "media" : Episode.objects.exclude(arc__filler=True),
            "sagas" : Saga.objects.all()
        }

        return render(request, "anime.html", context)

def error_404(request, exception):
        return render(request, "404.html")