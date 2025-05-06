from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from hackcollect.permissions import IsOwnerOrReadOnly
from .models import Rating
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import RatingSerializer
from rest_framework.exceptions import PermissionDenied


class RatingListCreateView(generics.ListCreateAPIView):
    """
    Check if the person liked their own hack or if the
    person is logged out.
    """
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['hack', 'owner']

    def perform_create(self, serializer):
        hack = serializer.validated_data['hack']
        if hack.owner == self.request.user:
            raise PermissionDenied("You cannot rate your own Hack!")

        if self.request.user.is_authenticated:
            serializer.save(owner=self.request.user)
        else:
            raise PermissionDenied("Only registered users can vote!")


class RatingRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [IsOwnerOrReadOnly]
