"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from rest_framework.routers import DefaultRouter

from core import views

router = DefaultRouter()
router.register(r'exams', views.ExamViewSet, basename='exams')
router.register(r'exams/(?P<exam_id>\d+)/themes', views.ExamThemeViewSet, basename='exams_themes')
router.register(r'themes/(?P<theme_id>\d+)/questions', views.QuestionViewSet, basename='questions')
router.register(r'exams_practice', views.ExamPracticeViewSet, basename='exam_practice')
urlpatterns = []

urlpatterns += router.urls
