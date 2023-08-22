from django.urls import path

from .views import GetAllContactForm, CreateContactForm

urlpatterns = [
    path('', GetAllContactForm.as_view(), name='get_all_contact_forms'),
    path('new/', CreateContactForm.as_view(), name='create_new_contact_form')
]
