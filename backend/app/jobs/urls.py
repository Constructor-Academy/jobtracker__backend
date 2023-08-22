from django.urls import path

from app.jobs.views.invites import CreateInvite
from app.jobs.views.jobs import GetCreateJobs, UpdateJobs, GetJobPreview, NotifyAdminsAcceptedJob, UpdateSingleJob, \
    GetJobSuggestionsFromSkillgap, DeleteRejectedJobs

urlpatterns = [
    path('', GetCreateJobs.as_view()),
    path('update/', UpdateJobs.as_view()),
    path('update/<str:pk>/', UpdateSingleJob.as_view()),
    path('get-preview/', GetJobPreview.as_view()),
    path('invite/', CreateInvite.as_view()),
    path('notify-admins-accepted-job/', NotifyAdminsAcceptedJob.as_view()),
    path('suggestions/', GetJobSuggestionsFromSkillgap.as_view()),
    path('clear-rejected/', DeleteRejectedJobs.as_view())
]
