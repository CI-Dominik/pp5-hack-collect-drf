from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from hackcollect.permissions import IsOwnerOrReadOnly
from .models import Rating
from .serializers import RatingSerializer


class RatingListCreateView(generics.ListCreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(owner=self.request.user)
        else:
            raise PermissionError("Only registered users can leave a rating!")


class RatingRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [IsOwnerOrReadOnly]
