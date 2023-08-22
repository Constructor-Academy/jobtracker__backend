from rest_framework import serializers

from app.jobs.models import Job, AdminInvite


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'
        read_only_fields = ['id', 'image']


class JobFixedIndexSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'
        read_only_fields = ['id', 'image', 'index']


class AdminInviteSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminInvite
        fields = ['admin_email']
