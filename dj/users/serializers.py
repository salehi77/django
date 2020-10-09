from rest_framework import serializers
from .models import User
from djoser.serializers import UserSerializer


class MyUserSerializer(UserSerializer):
    class Meta:
        model = User
        fields = ('id',
                  #   'password',
                  'last_login',
                  #   'is_superuser',
                  'first_name',
                  'last_name',
                  #   'is_staff',
                  'is_active',
                  'date_joined',
                  'email',
                  'groups',
                  #   'user_permissions'
                  )
        read_only_fields = ('id', 'last_login', 'date_joined', 'is_active',)
