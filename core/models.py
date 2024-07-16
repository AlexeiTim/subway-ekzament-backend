from django.db import models


class Exam(models.Model):
    title = models.CharField('Название экзамена', max_length=255)
    description = models.TextField('Описание экзамена', default='', blank=True)

    def __str__(self):
        return f'{self.title}'


class Theme(models.Model):
    title = models.CharField('Название темы экзамена', max_length=255)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='themes')

    def __str__(self):
        return f'{self.title}'


class Question(models.Model):
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField('Текст вопроса')


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    text = models.TextField('Текст вопроса')
    is_correct = models.BooleanField(default=False)



