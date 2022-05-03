from rest_framework import serializers
from django.contrib.auth import get_user_model
from core.models import Tweet, Like, SaveTweet


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'username', 'firstname', 'lastname',
                  'bio', 'join_date', 'picture')


class UserSignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'username',
                  'firstname', 'lastname', 'password')


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ('id', 'tweet', 'user')


class TweetSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    firstname = serializers.ReadOnlyField(source='user.firstname')
    lastname = serializers.ReadOnlyField(source='user.lastname')
    likes = LikeSerializer(many=True, read_only=True)

    class Meta:
        model = Tweet
        fields = ('id', 'content', 'date_created', 'user', 'firstname', 'lastname', 'likes')


class SaveTweetSerializer(serializers.ModelSerializer):
    tweet = TweetSerializer(read_only=True)

    class Meta:
        model = SaveTweet
        fields = ('id', 'tweet')
