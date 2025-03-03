from django.urls import path
from categories import views

urlpatterns = [
    path('categories/', views.CategoryListCreateView.as_view()),
    path(
        'categories/<int:pk>/',
        views.CategoryRetrieveUpdateDestroyView.as_view()
        ),
]
