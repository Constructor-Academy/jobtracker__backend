from django.urls import path
from .views import GetAllFeedback, CreateFeedback


urlpatterns = [
    path('', GetAllFeedback.as_view(), name='get_all_feedback'),
    path('new/', CreateFeedback.as_view(), name='create_new_feedback')
]
