from rest_framework.views import APIView
from rest_framework import authentication, permissions
from rest_framework_simplejwt.views import TokenViewBase
from .serializers import TokenDestroySerializer



class TokenDestroyView(TokenViewBase):
    """
    Takes a refresh type JSON web token and add it to Blacklist.
    """
    serializer_class = TokenDestroySerializer
    # permission_classes = [permissions.IsAuthenticated]
