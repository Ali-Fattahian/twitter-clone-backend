from rest_framework import serializers
from django.contrib.auth import get_user_model
from core.models import Tweet


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'username', 'firstname', 'lastname',
                  'password', 'bio', 'join_date', 'picture')


class TweetSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Tweet
        fields = ('id', 'content', 'date_created', 'user')
