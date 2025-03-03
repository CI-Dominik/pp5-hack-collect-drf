from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from hackcollect.permissions import IsOwnerOrReadOnly
from .models import Rating
from .serializers import RatingSerializer


class RatingListCreateView(generics.ListCreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [IsAuthenticated]


class RatingRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [IsOwnerOrReadOnly]
