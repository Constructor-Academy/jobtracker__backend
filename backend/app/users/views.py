import datetime
import math
# import os
# import logging

from django.contrib.auth import get_user_model
from django_weasyprint import WeasyTemplateView
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView
from rest_framework.permissions import IsAuthenticated

from app.global_permissions import IsStudentsBookletAuthor
# from app.settings import BASE_DIR
from app.users.serializers import UserSerializer, StudentBookletSerializer
from rest_framework.parsers import JSONParser
from app.users.parsers import CustomMultipartParser

User = get_user_model()


class ListUsers(ListAPIView):
    """
    List all Users.
    """
    serializer_class = UserSerializer

    def get_queryset(self):
        return self.request.user.administered_users.all()


class ListMyAdmins(ListAPIView):
    """
    List admins of logged in user.
    """
    serializer_class = UserSerializer

    def get_queryset(self):
        return self.request.user.admins.all()


class RetrieveUser(RetrieveAPIView):
    """
    Retrieve one User.
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_url_kwarg = 'user_id'


class RetrieveUpdateDestroyLoggedInUser(RetrieveUpdateDestroyAPIView):
    """
    get:
    Retrieve logged-in User.

    update:
    Update User.

    delete:
    Delete logged-in User.
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()
    parser_classes = (JSONParser, CustomMultipartParser, )

    def get_object(self):
        return self.request.user


class RetrieveUserCV(RetrieveAPIView):
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class StudentBookletView(GenericAPIView, WeasyTemplateView):
    permission_classes = [IsAuthenticated, IsStudentsBookletAuthor]
    template_name = 'users/booklet.html'

    def get_students_email_list(self, students_email_string):
        email_list = [email.strip() for email in students_email_string.split(',')]
        return email_list

    def get_students_data(self, students_emails):
        students = User.objects.filter(email__in=students_emails).order_by('last_name')
        serializer = StudentBookletSerializer(students, many=True)
        return serializer.data

    def get_students_groups(self, students, amount_per_group=3):
        groups = []
        groups_amount = math.ceil(len(students) / amount_per_group)
        for i in range(groups_amount):
            start = i * 3
            end = (i + 1) * 3
            groups.append(students[start:end])
        return groups

    def get_pdf_filename(self):
        today = datetime.date.today()
        date = f'{today.year}_{today.month:02d}_{today.day:02d}'
        title = self.request.query_params.get('title') or 'booklet'
        return f'{date}_{title}'

    def get_context_data(self, **kwargs):
        kwargs.setdefault('view', self)
        if self.extra_context is not None:
            kwargs.update(self.extra_context)
        title = self.request.query_params.get('title', None)
        students_emails_string = self.request.query_params.get('students', '')
        students_emails = self.get_students_email_list(students_emails_string)
        students_data = self.get_students_data(students_emails)
        students = self.get_students_groups(students=students_data)
        kwargs.update({'title': title, 'students': students})
        kwargs.update({'title': title})
        return kwargs

    def get(self, request, *args, **kwargs):
        # logger = logging.getLogger('weasyprint')
        # logger.addHandler(logging.FileHandler(os.path.join(BASE_DIR, 'tmp/weasyprint.log')))
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)
