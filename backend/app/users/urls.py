from django.urls import path

from app.users.views import ListUsers, RetrieveUser, ListMyAdmins, RetrieveUpdateDestroyLoggedInUser, RetrieveUserCV, \
    StudentBookletView

urlpatterns = [
    path('', ListUsers.as_view(), name='list-users'),
    path('<int:user_id>/', RetrieveUser.as_view(), name='retrieve-user'),
    path('me/', RetrieveUpdateDestroyLoggedInUser.as_view(), name='retrieve-update-destroy-logged-in-user'),
    path('me/admins/', ListMyAdmins.as_view()),
    path('me/cv/', RetrieveUserCV.as_view()),
    path('booklet/', StudentBookletView.as_view(), name='users-student-booklet'),
]
