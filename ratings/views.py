from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from hackcollect.permissions import IsOwnerOrReadOnly
from .models import Rating
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import RatingSerializer


class RatingListCreateView(generics.ListCreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['hack']

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            hack_id = serializer.validated_data.get('hack').id
            hack_owner = Rating.objects.get(id=hack_id).owner

            if hack_owner == self.request.user:
                raise PermissionError("You cannot vote on your own Hack!")

            serializer.save(owner=self.request.user)
        else:
            raise PermissionError("Only registered users can vote!")


class RatingRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [IsOwnerOrReadOnly]
