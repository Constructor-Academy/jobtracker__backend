from django.urls import path

from app.curriculums.views import CreateEducation, ChangeDeleteEducation, \
    CreateExperience, ChangeDeleteExperience, \
    CreateLanguage, ChangeDeleteLanguage, \
    CreateSkill, ChangeDeleteSkill, CreateCategory, ChangeDeleteCategory, CreateEvent, ChangeDeleteEvent

urlpatterns = [
    path('education/', CreateEducation.as_view()),
    path('education/<uuid:pk>/', ChangeDeleteEducation.as_view()),
    path('experience/', CreateExperience.as_view()),
    path('experience/<uuid:pk>/', ChangeDeleteExperience.as_view()),
    path('language/', CreateLanguage.as_view()),
    path('language/<uuid:pk>/', ChangeDeleteLanguage.as_view()),
    path('skill/', CreateSkill.as_view()),
    path('skill/<uuid:pk>/', ChangeDeleteSkill.as_view()),
    path('category/', CreateCategory.as_view()),
    path('category/<uuid:pk>/', ChangeDeleteCategory.as_view()),
    path('event/', CreateEvent.as_view()),
    path('event/<uuid:pk>/', ChangeDeleteEvent.as_view()),
]
