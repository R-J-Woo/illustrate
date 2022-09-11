from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import Illustrates
from .serializers import IllustCreateSerializer, IllustSerializer
from .permissions import CustomReadOnly
from users.models import Profile
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.


class IllustViewSet(viewsets.ModelViewSet):
    queryset = Illustrates.objects.all()
    permission_classes = [CustomReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['illustrator', 'likes']

    def get_serializer_class(self):
        if self.action == 'list' or 'retrieve':
            return IllustSerializer
        return IllustCreateSerializer

    def perform_create(self, serializer):
        profile = Profile.objects.get(user=self.request.user)
        serializer.save(illustrator=self.request.user, profile=profile)
