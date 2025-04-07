from rest_framework import generics, permissions, filters
from hackcollect.permissions import IsOwnerOrReadOnly
from .models import Hack
from django.db.models import Avg, Count
from django.db.models.functions import Coalesce
from .serializers import HackSerializer
from django.db.models import FloatField


class HackList(generics.ListCreateAPIView):
    serializer_class = HackSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Hack.objects.all().annotate(
        average_rating=Coalesce(
            Avg('rating__rating'), 0, output_field=FloatField()
            ),
        comments_count=Count('comments', distinct=True)
    ).order_by('-created_at')

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = [
        'owner__rating__owner',
    ]
    search_fields = [
        'owner__username',
        'title',
    ]

    ordering_fields = [
        'average_rating',
        'category'
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class HackDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = HackSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Hack.objects.all().annotate(
        average_rating=Coalesce(
            Avg('rating__rating'), 0, output_field=FloatField()
            ),
        comments_count=Count('comments', distinct=True)
    ).order_by('-created_at')
