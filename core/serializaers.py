from rest_framework import serializers

from core import models


class ExamSerializer(serializers.ModelSerializer):
    themes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = models.Exam
        fields = '__all__'


class ExamThemeSerializer(serializers.ModelSerializer):
    questions_count = serializers.SerializerMethodField()
    exam = ExamSerializer(read_only=True)

    class Meta:
        model = models.Theme
        fields = ['id', 'title', 'questions_count', 'exam']

    @staticmethod
    def get_questions_count(obj):
        return obj.questions.count()


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Answer
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, read_only=True)
    theme = ExamThemeSerializer(read_only=True)
    class Meta:
        model = models.Question
        fields = '__all__'
