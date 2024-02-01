from django.shortcuts import render
from rest_framework import viewsets
from core import models, serializaers


def index(request):
    return render(request, 'core/index.html')


class ExamViewSet(viewsets.ModelViewSet):
    queryset = models.Exam.objects.all()
    serializer_class = serializaers.ExamSerializer

