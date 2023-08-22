from rest_framework import status
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView
from rest_framework.mixins import CreateModelMixin

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from app.curriculums.models.category import Category
from app.curriculums.models.event import Event
from app.curriculums.permissions import BelongsToUserOrAdmin, BelongsToUserByCategoryOrAdmin, \
    CategoryBelongsToUserOrAdmin

from app.curriculums.serializers import EducationSerializer, \
    ExperienceSerializer, \
    LanguageSerializer, \
    SkillSerializer, CategorySerializer, EventSerializer
from app.curriculums.models import Education, Experience, Language, Skill


class CreateEducation(CreateAPIView):
    """
    Create an education
    """
    serializer_class = EducationSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ChangeDeleteEducation(RetrieveUpdateDestroyAPIView):
    """
    Patch or delete an education
    """
    permission_classes = [IsAuthenticated,
                          BelongsToUserOrAdmin]
    http_method_names = ['patch', 'delete']
    serializer_class = EducationSerializer
    queryset = Education.objects.all()


class CreateExperience(CreateAPIView):
    """
    Create an experience
    """
    serializer_class = ExperienceSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ChangeDeleteExperience(RetrieveUpdateDestroyAPIView):
    """
    Patch or delete an experience
    """
    permission_classes = [IsAuthenticated,
                          BelongsToUserOrAdmin]
    http_method_names = ['patch', 'delete']
    serializer_class = ExperienceSerializer
    queryset = Experience.objects.all()


class CreateLanguage(CreateAPIView):
    """
    Create a language
    """
    permission_classes = [IsAuthenticated,
                          BelongsToUserOrAdmin]
    serializer_class = LanguageSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ChangeDeleteLanguage(RetrieveUpdateDestroyAPIView):
    """
    Patch or delete a language
    """
    permission_classes = [IsAuthenticated,
                          BelongsToUserOrAdmin]
    http_method_names = ['patch', 'delete']
    serializer_class = LanguageSerializer
    queryset = Language.objects.all()


class CreateSkill(CreateAPIView):
    """
    Create a skill
    """
    serializer_class = SkillSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ChangeDeleteSkill(RetrieveUpdateDestroyAPIView):
    """
    Patch or delete a skill
    """
    permission_classes = [BelongsToUserOrAdmin]
    http_method_names = ['patch', 'delete']
    serializer_class = SkillSerializer
    queryset = Skill.objects.all()


class CreateCategory(CreateAPIView):
    """
    Create a skill
    """
    serializer_class = CategorySerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ChangeDeleteCategory(RetrieveUpdateDestroyAPIView):
    """
    Patch or delete a skill
    """
    permission_classes = [BelongsToUserOrAdmin]
    http_method_names = ['patch', 'delete']
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CreateEvent(GenericAPIView, CreateModelMixin):
    """
    Create a skill
    """
    serializer_class = EventSerializer
    permission_classes = [CategoryBelongsToUserOrAdmin]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        events = Event.objects.filter(category=request.data.get('category'), category__user=request.user)
        return Response(EventSerializer(events, many=True).data, status=status.HTTP_201_CREATED, headers=headers)


class ChangeDeleteEvent(RetrieveUpdateDestroyAPIView):
    """
    Patch or delete a skill
    """
    permission_classes = [BelongsToUserByCategoryOrAdmin]
    http_method_names = ['patch', 'delete']
    serializer_class = EventSerializer
    queryset = Event.objects.all()
