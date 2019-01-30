from rest_framework import serializers
from . import models
from rest_auth.models import TokenModel
from rest_auth.serializers import UserDetailsSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = ('email', 'first_name', 'username', 'last_name', 'date_joined' )

class TokenSerializer(serializers.ModelSerializer):
    """
    Serializer for Token model.
    """

    class Meta:
        model = TokenModel
        fields = ('key', 'user')
