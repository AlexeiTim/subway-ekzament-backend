from rest_framework import serializers

from core import models


class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Exam
        fields = '__all__'


class ExamThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Theme
        fields = ['id', 'title']
