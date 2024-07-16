import random

from django.shortcuts import render
from rest_framework import viewsets, filters
from rest_framework.response import Response

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
    filter_backends = (filters.SearchFilter,)
    search_fields = ('title',)

    def get_queryset(self):
        queryset = models.Theme.objects.filter(exam_id=self.kwargs['exam_id'])
        return queryset


class QuestionViewSet(viewsets.ModelViewSet):
    serializer_class = serializaers.QuestionSerializer

    def get_queryset(self):
        queryset = models.Question.objects.filter(theme_id=self.kwargs['theme_id'])
        questions_count = self.request.query_params.get('questions_count')
        if questions_count:
            questions_count = int(questions_count)
            queryset = random.sample(list(queryset), min(len(queryset), questions_count))
        return queryset


class ExamPracticeViewSet(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        exam = models.Exam.objects.get(pk=pk)
        themes = models.Theme.objects.filter(exam_id=pk)
        questions = models.Question.objects.filter(theme__in=themes)

        themes_data = serializaers.ExamThemeSerializer(themes, many=True).data
        exam_data = serializaers.ExamSerializer(exam).data
        questions_data = serializaers.QuestionSerializer(questions, many=True).data

        return Response({
            'exam': exam_data,
            'themes': themes_data,
            'questions': questions_data,
        })

