from django.shortcuts import render
from .models import Saga, Arc, Chapter, Episode
from django.views.generic import ListView

class MangaTimeLineView(ListView):

    def get(self, request, *args, **kwargs):

        context = {
            "years": range(1997, 2024),
            "media" : Chapter.objects.all(),
            "sagas" : Saga.objects.all()
        }

        return render(request, "manga.html", context)
    
    def search_year(request, slug= None):

        context = {}

        if slug is None or int(slug) not in range(1997, 2024):
            return render(request, "404.html")
        else:
            context["years"] = [slug]
            context["media"] = Chapter.objects.filter(year=slug)
            return render(request, "manga.html", context)
        
    def search_saga(request, slug= None):

        context = {}
    
        search = Chapter.objects.filter(arc__saga__id=slug)

        if slug is None or search.count() == 0:
            return render(request, "404.html")
        else:
            context["media"] = search
            context["sagas"] = Saga.objects.filter(id=slug)
            return render(request, "manga.html", context)
    

class AnimeTimeLineView(ListView):

    def get(self, request, *args, **kwargs):

        context = {
            "years": range(1999, 2024),
            "media" : Episode.objects.all(),
            "sagas" : Saga.objects.all()
        }

        return render(request, "anime.html", context)
    
    def nofiller(request):

        context = {
            "years": range(1999, 2024),
            "media" : Episode.objects.exclude(arc__filler=True),
            "sagas" : Saga.objects.all()
        }

        return render(request, "anime.html", context)

    def search_year(request, slug= None):

        context = {}

        if slug is None or int(slug) not in range(1999, 2024):
            return render(request, "404.html")
        else:
            context["years"] = [slug]
            context["media"] = Episode.objects.filter(year=slug)
            return render(request, "anime.html", context)
        
    def search_saga(request, slug= None):

        context = {}
    
        search = Episode.objects.filter(arc__saga__id=slug)

        if slug is None or search.count() == 0:
            return render(request, "404.html")
        else:
            context["media"] = search
            return render(request, "anime.html", context)

def error_404(request, exception):
        return render(request, "404.html")