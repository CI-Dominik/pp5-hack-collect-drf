from django.urls import path
from hacks import views

urlpatterns = [
    path('hacks/', views.HackList.as_view()),
    path('hacks/<int:pk>', views.HackDetail.as_view())
]
