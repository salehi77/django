from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import authentication, permissions, views
from rest_framework_simplejwt.views import TokenViewBase
from .serializers import TokenDestroySerializer



class TokenDestroyView(TokenViewBase):
    """
    Takes a refresh type JSON web token and add it to Blacklist.
    """
    serializer_class = TokenDestroySerializer
    # permission_classes = [permissions.IsAuthenticated]


class IndexView(views.APIView):
    def get(self, request):
        return render(request, 'users/index.html')
