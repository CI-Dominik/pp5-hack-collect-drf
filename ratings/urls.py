from django.urls import path
from .views import RatingListCreateView, RatingRetrieveUpdateDestroyView

urlpatterns = [
    path('ratings/', RatingListCreateView.as_view()),
    path('ratings/<pk>/', RatingRetrieveUpdateDestroyView.as_view()),
]