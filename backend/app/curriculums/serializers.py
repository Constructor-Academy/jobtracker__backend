from rest_framework import serializers
from app.curriculums.models import Education, Experience, Language, Skill
from app.curriculums.models.category import Category
from app.curriculums.models.event import Event


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'
        read_only_fields = ['user', 'id']
        ordering = ['-end_date']


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'
        read_only_fields = ['user', 'id']
        ordering = ['-end_date']


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ['tag', 'level']
        read_only_fields = ['user', 'id']


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['tag', 'level']
        read_only_fields = ['user', 'id']


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
        read_only_fields = ['user', 'id']


class CategorySerializer(serializers.ModelSerializer):
    events = EventSerializer(many=True, required=False)

    class Meta:
        model = Category
        fields = ['id', 'name', 'events']
        read_only_fields = ['user', 'id']
