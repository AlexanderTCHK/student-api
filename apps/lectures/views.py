from rest_framework import viewsets
from .serializers import LectureSerializer
from .models import Lecture


class LectureViewSet(viewsets.ModelViewSet):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer
