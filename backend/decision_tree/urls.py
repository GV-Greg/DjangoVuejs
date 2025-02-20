from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProgramViewSet, SubjectViewSet, QuestionViewSet, AnswerViewSet

router = DefaultRouter()
router.register(r'programs', ProgramViewSet)
router.register(r'subjects', SubjectViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'answers', AnswerViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
