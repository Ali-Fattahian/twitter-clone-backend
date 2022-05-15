from rest_framework import serializers
from django.contrib.auth import get_user_model
import datetime
from core.models import Tweet, Like, SaveTweet, Reply
from users.models import Follow
from .utils import  datetime_subtractor


class ProfileSerializer(serializers.ModelSerializer):
    date_joined = serializers.SerializerMethodField('get_date_joined')
    tweet_number = serializers.SerializerMethodField('get_tweet_number')
    follows = serializers.SerializerMethodField('get_follows')

    def get_date_joined(self, obj):
        """A property that shows join date and time of a user in a usefull way"""
        now = datetime.datetime.now()
        now_aware = now.replace(tzinfo=datetime.timezone.utc)
        return {'date_joined_ago': datetime_subtractor(now_aware, obj.join_date), 'date_joined': obj.join_date}

    def get_tweet_number(self, obj):
        """Get the number of tweets created by this user"""
        return obj.tweets.all().count()

    def get_follows(self, obj):
        followers_objs = obj.followers.all()
        followers = []
        for follower_obj in followers_objs:
            followers.append(follower_obj.follower.username)
        followings_objs = obj.follows.all()
        followings = []
        for following_obj in followings_objs:
            followings.append(following_obj.user.username)
        return {'followings_count': len(followings), 'followers_count': len(followers)}


    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'username', 'firstname', 'lastname',
                  'bio', 'join_date', 'picture', 'date_joined', 'tweet_number', 'follows')


class UserSignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'username',
                  'firstname', 'lastname', 'password')


class LikeSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    tweet = serializers.ReadOnlyField(source='tweet.id')
    class Meta:
        model = Like
        fields = ('id', 'tweet', 'user')
        

class FollowSerializer(serializers.ModelSerializer):
    follower = serializers.ReadOnlyField(source='follower.username')

    class Meta:
        model = Follow
        fields = ('id', 'user', 'follower')

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


class ReplySerializer(serializers.ModelSerializer):
    user = ProfileSerializer(read_only=True)
    tweet = serializers.ReadOnlyField(source='tweet.id')
    date_created = serializers.SerializerMethodField('get_date_created')

    def get_date_created(self, obj):
        now = datetime.datetime.now()
        now_aware = now.replace(tzinfo=datetime.timezone.utc)
        return {'created_ago': datetime_subtractor(now_aware, obj.date_created), 'created': obj.date_created}

    class Meta:
        model = Reply 
        fields = ('id', 'text', 'user', 'tweet', 'date_created')
        