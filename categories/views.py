from rest_framework import generics, status
from rest_framework.permissions import IsAdminUser
from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.response import Response
from .models import Category
from .serializers import CategorySerializer


class ReadOnlyOrAdmin(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user and request.user.is_staff


class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [ReadOnlyOrAdmin]

    def perform_create(self, serializer):
        serializer.save()


class CategoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'pk'
    permission_classes = [IsAdminUser]

    def destroy(self, request, *args, **kwargs):
        if Category.objects.count() <= 1:
            return Response(
                {"detail": "Cannot delete the last remaining category."},
                status=status.HTTP_400_BAD_REQUEST
            )
        return super().destroy(request, *args, **kwargs)
