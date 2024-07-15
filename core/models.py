from django.db import models


class Exam(models.Model):
    title = models.CharField('Название экзамена', max_length=255)
    description = models.TextField('Описание экзамена', default='', blank=True)

    def __str__(self):
        return f'{self.title}'


class Theme(models.Model):
    title = models.CharField('Название темы экзамена', max_length=255)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'
