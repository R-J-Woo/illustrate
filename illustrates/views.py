from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
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


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def like_illustrate(request, pk):
    illustrate = get_object_or_404(Illustrates, pk=pk)
    if request.user in illustrate.likes.all():
        illustrate.likes.remove(request.user)
    else:
        illustrate.likes.add(request.user)

    return Response({'status': 'ok'})
