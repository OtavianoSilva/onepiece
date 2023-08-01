from django.shortcuts import render
from .models import Arc, Chapter
from django.views.generic.detail import DetailView

class ArcView(DetailView):
    template_name = "index.html"
    model = Arc

    context = {
        'chapters' : Chapter.objects.all()
    }

    def get(self, request, *args, **kwargs):
        return render(request, "index.html", self.context)