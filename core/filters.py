import django_filters

from core import models


class ExamFilter(django_filters.FilterSet):
    class Meta:
        model = models.Exam
