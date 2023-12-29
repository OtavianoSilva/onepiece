from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from ..models import Chapter
from ..serializers import ChapterSerializer

@api_view()
def chapter_overview(request):
    objects = Chapter.objects.all()
    serializer = ChapterSerializer(instance=objects, many=True)
    return Response(serializer.data)

@api_view()
def chapter_detail(request, pk):
    objects = get_object_or_404(
        Chapter.objects.all(),
        pk=pk,
    )
    serializer = ChapterSerializer(instance=objects, many=False)
    return Response(serializer.data)