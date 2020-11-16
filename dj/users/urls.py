from django.urls import path

from . import views

urlpatterns = [
    path('jwt/destroy/', views.TokenDestroyView.as_view()),
    path('index/', views.IndexView.as_view()),
]
