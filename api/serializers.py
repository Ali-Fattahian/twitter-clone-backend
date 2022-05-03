from rest_framework import serializers
from django.contrib.auth import get_user_model
import datetime
from core.models import Tweet, Like, SaveTweet
from .utils import  datetime_subtractor


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
    date_created = serializers.SerializerMethodField('get_date_created')

    def get_date_created(self, obj):
        """A property that shows creation date and time of a tweet in a usefull way"""

        now = datetime.datetime.now()
        # Add UTC to it so it's similar to django datetimefield default behavior
        now_aware = now.replace(tzinfo=datetime.timezone.utc)
        return {'created_ago': datetime_subtractor(now_aware, obj.date_created), 'created': obj.date_created}

    class Meta:
        model = Tweet
        fields = ('id', 'content', 'date_created', 'user',
                  'firstname', 'lastname', 'likes')


class SaveTweetSerializer(serializers.ModelSerializer):
    tweet = TweetSerializer(read_only=True)

    class Meta:
        model = SaveTweet
        fields = ('id', 'tweet')
