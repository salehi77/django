from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from djoser.serializers import UserSerializer
from .models import User
from shop.serializers import BookmarkSerializer


class TokenDestroySerializer(serializers.Serializer):
    refresh = serializers.CharField()

    def validate(self, attrs):
        refresh = RefreshToken(attrs['refresh'])

        try:
            refresh.blacklist()
        except AttributeError:
            pass

        return {}


class MyUserSerializer(UserSerializer):
    bookmarks = BookmarkSerializer(many=True)

    class Meta:
        model = User
        fields = ('id',
                  #   'password',
                  'last_login',
                  #   'is_superuser',
                  'first_name',
                  'avatar',
                  'last_name',
                  #   'is_staff',
                  'is_active',
                  'date_joined',
                  'email',
                  'groups',
                  #   'user_permissions'
                  'bookmarks',
                  )
        read_only_fields = ('id', 'last_login', 'date_joined', 'is_active',)
