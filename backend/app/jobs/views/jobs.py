import json

import requests
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.generics import GenericAPIView, UpdateAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from webpreview import web_preview

from app.emails.signals import send_email
from app.jobs.models import Job
from app.jobs.permissions import JobsBelongToUserOrAdmin, JobBelongsToUserOrAdmin
from app.jobs.serializers import JobSerializer, JobFixedIndexSerializer
from app.users.serializers import UserSerializer, UserSkillGapSuggestionSerializer

User = get_user_model()


class GetCreateJobs(ListCreateAPIView):
    """
    get:
    List all Jobs of user
    """
    serializer_class = JobSerializer

    def get_queryset(self):
        if self.request.user.is_admin:
            return Job.objects.filter(user__id=int(self.request.query_params.get('user_id')))
        return Job.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UpdateJobs(GenericAPIView):
    serializer_class = JobSerializer
    queryset = Job.objects.all()
    permission_classes = [IsAuthenticated, JobsBelongToUserOrAdmin]

    def post(self, request, *args, **kwargs):
        for_user_id = request.data.get('for_user_id')
        if not for_user_id:
            return Response('User is required', status=status.HTTP_400_BAD_REQUEST)

        old_jobs = list(Job.objects.filter(user__id=for_user_id))
        serializer = self.get_serializer(data=request.data['jobs'], many=True)
        try:
            serializer.is_valid(raise_exception=True)
        except ValidationError as exc:
            invalid_job_errors = [obj for obj in exc.detail if bool(obj)][0]
            return Response(invalid_job_errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()

        for old_job in old_jobs:
            old_job.delete()

        return Response(serializer.data)


# this endpoint is to update content during editing / cover letter creation. Should not be used after a job has been moved with drag and drop
class UpdateSingleJob(UpdateAPIView):
    serializer_class = JobFixedIndexSerializer
    queryset = Job.objects.all()
    permission_classes = [IsAuthenticated, JobBelongsToUserOrAdmin]


# def extractResults(result):
#     return {
#         'sourceCol': result.source.droppableId,
#         'destCol': result.destination.droppableId,
#         'jobId': result.draggableId,
#         'sourceIndex': result.source.index,
#         'destIndex': result.destination.index,
#         'job': Job.objects.get(id=result['draggableId'])
#     }
#
#
# class UpdateJobsv2(GenericAPIView):
#     serializer_class = JobSerializer
#     queryset = Job.objects.all()
#     permission_classes = [IsAuthenticated, JobsBelongToUserOrAdmin, JobsNotEmpty]
#
#     def post(self, request, *args, **kwargs):
#         result = request.data
#
#         # If item dragged outside of drop columns, do nothing.
#         if not result.get('destination', False):
#             return Response(self.get_serializer(instance=Job.objects.filter(user__id=Job.objects.get(id=result['draggableId']).user_id), many=True).data)
#
#         # Extract drag & drop event data
#         extractedResult = extractResults(result);
#         return Response(self.get_serializer(instance=Job.objects.filter(user__id=Job.objects.get(id=result['draggableId']).user_id), many=True).data)


class GetJobPreview(GenericAPIView):
    def get(self, request, *args, **kwargs):
        url = request.data.get('url')
        title, description, image = web_preview(url)
        res = {
            'title': title,
            'description': description,
            'image': image
        }
        return Response(res)


class NotifyAdminsAcceptedJob(GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        user = request.user
        admins = user.admins.all()
        for admin in admins:
            send_email.send(sender=Job, request=request, to=admin.email, email_type='notify_admins_accepted_job',
                            user_email=user.email)
        return Response(status=200)


class GetJobSuggestionsFromSkillgap(APIView):
    """
    get:
    Gets jobs based on data from user profile stored in the database

    post:
    Gets jobs based on uploaded cv
    """

    def get(self, request, *args, **kwargs):
        backend_url = 'https://jobs.jobtracker.ai/get_skill_gap'

        serializer = UserSkillGapSuggestionSerializer(request.user)
        # Pop the skills to imitate results based on an empty profile for FE development purpose
        # content = serializer.data
        # content.pop('skills')
        # data = json.dumps(content)
        if serializer.data.get('user_description').strip() == "" and \
                len(serializer.data.get('experiences')) == 0 and \
                len(serializer.data.get('educations')) == 0 and \
                len(serializer.data.get('languages')) == 0 and \
                len(serializer.data.get('skills')) == 0:
            return Response(status=status.HTTP_204_NO_CONTENT)
        data = json.dumps(serializer.data)
        try:
            r = requests.post(url=backend_url,
                              data=data,)
            res = Response(json.loads(r.content), status=r.status_code)
        except Exception as e:
            res = Response({"error": True, "message": str(e)}, status=500)
        return res


class DeleteRejectedJobs(GenericAPIView):
    permission_classes = [IsAuthenticated, JobBelongsToUserOrAdmin]

    def delete(self, request, *args, **kwargs):
        user = self.request.data.get('for_user')
        queryset = Job.objects.filter(user=user, status='RJ')
        queryset.delete()
        return Response(status=204)
