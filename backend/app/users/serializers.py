import datetime

from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from app.curriculums.serializers import ExperienceSerializer, \
    EducationSerializer, \
    LanguageSerializer, \
    SkillSerializer, CategorySerializer

from app.curriculums.models import Language, Skill
from rest_framework.utils import model_meta

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    experiences = SerializerMethodField()
    educations = SerializerMethodField()
    languages = LanguageSerializer(many=True)
    skills = SkillSerializer(many=True)
    jobs_count = SerializerMethodField()
    interviews_count = SerializerMethodField()
    is_working = SerializerMethodField()
    categories = SerializerMethodField()

    def get_jobs_count(self, obj):
        return obj.jobs.all().count()

    def get_interviews_count(self, obj):
        return obj.jobs.filter(status='IN').count()

    def get_is_working(self, obj):
        return obj.jobs.filter(status='AC').count() > 0

    def get_experiences(self, instance):
        experiences = instance.experiences.all().order_by('-end_date')
        return ExperienceSerializer(experiences, many=True).data

    def get_educations(self, instance):
        educations = instance.educations.all().order_by('-end_date')
        return EducationSerializer(educations, many=True).data

    def get_categories(self, instance):
        categories = instance.categories.all().order_by('created')
        return CategorySerializer(categories, many=True).data

    def update(self, instance, validated_data):
        info = model_meta.get_field_info(instance)

        m2m_fields = []
        for attr, value in validated_data.items():
            if attr in info.relations and info.relations[attr].to_many:
                m2m_fields.append((attr, value))
            else:
                setattr(instance, attr, value)

        if 'languages' in validated_data:
            instance.languages.all().delete()
            language_items = sorted(validated_data.pop('languages'), key=lambda k: k['level'], reverse=True)
            sorted_language_items = []
            # sorts languages by the following order NA, PR, IM, BA (not necessary for skills)
            for item in language_items:
                if item['level'] == "NA":
                    sorted_language_items.insert(0, item)
                else:
                    sorted_language_items.append(item)

            for language in sorted_language_items:
                Language.objects.create(user=instance, **language)

        if 'skills' in validated_data:
            instance.skills.all().delete()
            skill_items = sorted(validated_data.pop('skills'), key=lambda k: k['level'], reverse=True)

            for skill in skill_items:
                Skill.objects.create(user=instance, **skill)

        instance.save()
        return instance

    class Meta:
        model = User
        fields = ['id',
                  'email',
                  'first_name',
                  'last_name',
                  'username',
                  'street',
                  'zip',
                  'city',
                  'country',
                  'phone',
                  'date_of_birth',
                  'user_description',
                  'final_project',
                  'nationality',
                  'permit',
                  'linkedin_profile',
                  'github_profile',
                  'actual_position',
                  'is_admin',
                  'is_booklet_author',
                  'last_login',
                  'avatar',
                  'jobs_count',
                  'interviews_count',
                  'is_working',
                  'experiences',
                  'educations',
                  'languages',
                  'skills',
                  'categories',
                  'job_search_area'
                  ]
        read_only_fields = ['email']
        ordering = ('educations__end_date',)


class UserSkillGapSuggestionSerializer(serializers.ModelSerializer):
    experiences = SerializerMethodField()
    educations = SerializerMethodField()
    languages = LanguageSerializer(many=True)
    skills = SkillSerializer(many=True)

    def get_experiences(self, instance):
        experiences = instance.experiences.all().order_by('-end_date')
        return ExperienceSerializer(experiences, many=True).data

    def get_educations(self, instance):
        educations = instance.educations.all().order_by('-end_date')
        return EducationSerializer(educations, many=True).data

    class Meta:
        model = User
        fields = ['user_description',
                  'experiences',
                  'educations',
                  'languages',
                  'skills']


class StudentBookletSerializer(serializers.ModelSerializer):
    years_of_experience = SerializerMethodField()
    full_name = SerializerMethodField()
    languages = SerializerMethodField()
    skills = SerializerMethodField()
    job_search_area = SerializerMethodField()

    @staticmethod
    def get_years_of_experience(instance):
        years_of_experience = 0
        for experience in instance.experiences.all().values():
            end_date = experience.get('end_date') or datetime.date.today()
            years = (end_date - experience.get('start_date')).days / 365
            years_of_experience += years
        return int(years_of_experience)

    @staticmethod
    def get_full_name(instance):
        return instance.get_full_name()

    @staticmethod
    def get_languages(instance):
        def get_level(code):
            if code == 'BA':
                return 'Basic'
            if code == 'IM':
                return 'Intermediate'
            if code == 'PR':
                return 'Proficient'
            if code == 'NA':
                return 'Native'
            return code

        languages = [f"{item.get('tag')} <span>({get_level(item.get('level'))})</span>" for item in instance.languages.all().values()]
        languages_str = ', '.join(languages)
        return languages_str

    def get_skills(self, instance):
        skills = [item.get('tag') for item in instance.skills.all().values()]
        skills_str = ', '.join(skills)
        return skills_str

    @staticmethod
    def get_job_search_area(instance):
        return instance.job_search_area.title()

    class Meta:
        model = User
        fields = [
            'id',
            'avatar',
            'full_name',
            'email',
            'linkedin_profile',
            'github_profile',
            'user_description',
            'final_project',
            'years_of_experience',
            'languages',
            'skills',
            'job_search_area'
        ]
