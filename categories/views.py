from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from .models import Category
from .serializers import CategorySerializer


class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    permission_classes = [IsAdminUser]

    def perform_create(self, serializer):
        if self.request.user.is_staff:
            serializer.save()
        else:
            raise PermissionError("Only admins can create a category.")


class CategoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'pk'

    permission_classes = [IsAdminUser]
