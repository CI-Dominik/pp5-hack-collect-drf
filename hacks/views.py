from rest_framework import generics, permissions
from hackcollect.permissions import IsOwnerOrReadOnly
from .models import Hack
from .serializers import HackSerializer


class HackList(generics.ListCreateAPIView):
    serializer_class = HackSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Hack.objects.all().order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class HackDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = HackSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Hack.objects.all().order_by('-created_at')
