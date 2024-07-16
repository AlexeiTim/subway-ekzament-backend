from django.contrib import admin

from core import models

admin.site.register(models.Exam)
admin.site.register(models.Theme)
admin.site.register(models.Question)
admin.site.register(models.Answer)
