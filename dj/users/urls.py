from django.urls import path

from . import views

urlpatterns = [
    path('jwt/destroy/', views.TokenDestroyView.as_view()),
]
