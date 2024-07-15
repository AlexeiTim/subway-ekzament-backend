from django.shortcuts import render
from rest_framework import viewsets, filters, generics

from core import models, serializaers


def index(request):
    return render(request, 'core/index.html')


class ExamViewSet(viewsets.ModelViewSet):
    queryset = models.Exam.objects.all()
    serializer_class = serializaers.ExamSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('title',)


class ExamThemeViewSet(viewsets.ModelViewSet):
    serializer_class = serializaers.ExamThemeSerializer

    def get_queryset(self):
        queryset = models.Theme.objects.filter(exam_id=self.kwargs['exam_id'])
        return queryset
