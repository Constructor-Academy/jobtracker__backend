from rest_framework.generics import ListAPIView, CreateAPIView
from .models import Contact
from .serializers import ContactSerializer


class GetAllContactForm(ListAPIView):
    permission_classes = []
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()


class CreateContactForm(CreateAPIView):
    permission_classes = []
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()

    def perform_create(self, serializer):
        serializer.save()
