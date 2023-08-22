from rest_framework import serializers
from .models import Feedback
from ..users.serializers import UserSerializer


class FeedbackSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Feedback
        fields = '__all__'
        read_only_fields = ['user', 'id']
