from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Feedback
from .serializers import FeedbackSerializer


class GetAllFeedback(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.all()


class CreateFeedback(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
