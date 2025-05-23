from rest_framework import generics, permissions, filters
from hackcollect.permissions import IsOwnerOrReadOnly
from .models import Hack
from django.db.models import Avg, Count
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models.functions import Coalesce
from .serializers import HackSerializer
from django.db.models import FloatField


class HackList(generics.ListCreateAPIView):
    """
    View to return the Hacks. Only available for logged in users.
    The average_rating and comments_count gets added via annotate
    to display it in the frontend.
    Filters for rated content, following and category can be applied.
    Search is possible for the username and title.
    """
    serializer_class = HackSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Hack.objects.all().annotate(
        average_rating=Coalesce(
            Avg('ratings__rating'), 0, output_field=FloatField()
            ),
        comments_count=Count('comments', distinct=True)
    ).order_by('-created_at')

    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend
        ]
    filterset_fields = [
        'ratings__owner__profile',
        'owner__followed__owner__profile',
        'category__name',
        'owner__profile'
    ]
    search_fields = [
        'owner__username',
        'title',
    ]

    ordering_fields = [
        'average_rating',
        'category',
        'comments_count',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class HackDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = HackSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Hack.objects.all().annotate(
        average_rating=Coalesce(
            Avg('ratings__rating'), 0, output_field=FloatField()
            ),
        comments_count=Count('comments', distinct=True)
    ).order_by('-created_at')
