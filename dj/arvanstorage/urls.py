from django.urls import path

from . import views

urlpatterns = [
    path('', views.DocumentCreateView.as_view()),
]
