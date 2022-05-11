from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, filters, status
from django.contrib.auth import get_user_model
from datetime import datetime, timedelta, timezone
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
# from django.db.models import Q

from .serializers import LikeSerializer, UserSignUpSerializer, TweetSerializer, SaveTweetSerializer, ProfileSerializer, FollowSerializer
from core.models import Tweet, SaveTweet, Like
from users.models import Follow
from .utils import OnlySameUserCanEditMixin



class SignUpView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSignUpSerializer


class HomePageView(generics.ListCreateAPIView):
    serializer_class = TweetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            following_users = []
            tweets = Tweet.objects.none()
            follows = Follow.objects.filter(follower=self.request.user)
            for follow in follows:
                # now we have all the following users
                following_users.append(follow.user)
            for following_user in following_users:
                # now we have all the tweets from those users
                tweets = Tweet.objects.filter(user=following_user) | tweets
            return tweets.order_by('-date_created')
        return Tweet.objects.all().order_by('-date_created')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TweetListSearchResults(generics.ListAPIView):
    serializer_class = TweetSerializer
    search_fields = ['content']
    filter_backends = (filters.SearchFilter, )
    queryset = Tweet.objects.all()


class UserListSearchResults(generics.ListAPIView):
    serializer_class = ProfileSerializer
    search_fields = ['username', 'firstname', 'lastname', 'bio']
    filter_backends = (filters.SearchFilter, )
    queryset = get_user_model().objects.all()


class ExploreView(generics.ListAPIView):
    serializer_class = TweetSerializer
    now = datetime.now(timezone.utc)
    yesterday = now - timedelta(days=1)
    # Show the tweets from the last 24 hours
    queryset = Tweet.objects.filter(date_created__gte=yesterday)


class BookMarksView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = SaveTweetSerializer

    def get_queryset(self):
        # Returns all the savetweet objects
        return SaveTweet.objects.filter(user=self.request.user)


class SuggestedUsersView(generics.ListAPIView):
    serializer_class = ProfileSerializer

    def get_queryset(self):
        # if self.request.user.is_authenticated:
        #     followings = self.request.user.follows
        #     print(followings)
        # follows = Follow.objects.filter(~Q(follower=self.request.user)) # request.user is not the follower
        # users = get_user_model().objects.filter(~Q(self.request.user__in=followers))
        # suggests = []
        # for follow in follows:
        #     suggests.append(follow.user)
        # print(suggests)
        # return print(get_user_model().objects.exclude(user__in=followings)[:3])

        return get_user_model().objects.all()[:3]


class UserFollowView(generics.CreateAPIView):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(follower=self.request.user)


class UserUnfollowView(generics.DestroyAPIView):
    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Follow.objects.filter(follower=self.request.user)


class FollowCheckView(generics.RetrieveAPIView):
    queryset = Follow.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FollowSerializer
    
    def get_object(self):
        following_username = self.kwargs.get('username')
        following_user = get_object_or_404(get_user_model(), username=following_username)
        return get_object_or_404(Follow, user=following_user, follower=self.request.user)


class ProfileView(generics.RetrieveUpdateAPIView):
    queryset = get_user_model().objects.all()
    permission_classes = [OnlySameUserCanEditMixin]
    serializer_class = ProfileSerializer
    lookup_field = 'username'


class AddTweetView(generics.CreateAPIView):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class FollowersListView(generics.ListAPIView):
    serializer_class = ProfileSerializer

    def get_queryset(self):
        username = self.kwargs.get('username')
        user = get_object_or_404(get_user_model(), username=username)
        followers_objs = user.followers.all()
        followers = []
        for follower_obj in followers_objs:
            followers.append(follower_obj.follower)
        return followers


class FollowingsListView(generics.ListAPIView):
    serializer_class = ProfileSerializer

    def get_queryset(self):
        username = self.kwargs.get('username')
        user = get_object_or_404(get_user_model(), username=username)
        followings_objs = user.follows.all()
        followings = []
        for following_obj in followings_objs:
            followings.append(following_obj.user)
        return followings

class CreateLikeView(generics.CreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        tweet = get_object_or_404(Tweet, id=self.kwargs.get('tweet_id'))
        serializer.save(user=self.request.user, tweet=tweet)


class DeleteLikeView(generics.DestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        if self.get_object().user == self.request.user:
            return super().destroy(request, *args, **kwargs)
        return status.HTTP_401_UNAUTHORIZED


class ListLikeView(generics.ListAPIView):
    serializer_class = LikeSerializer
    
    def get_queryset(self):
        tweet = get_object_or_404(Tweet, id=self.kwargs.get('tweet_id'))
        return Like.objects.filter(tweet=tweet)


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)


        token['username'] = user.username
        # ...

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
