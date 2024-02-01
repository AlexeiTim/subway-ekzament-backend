from django.db import models


class Exam(models.Model):
    title = models.CharField('Название экзамена', max_length=255)

