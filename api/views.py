from rest_framework import generics, permissions, filters
from django.contrib.auth import get_user_model
from datetime import datetime, timedelta, timezone

from .serializers import UserSignUpSerializer, TweetSerializer, SaveTweetSerializer, ProfileSerializer
from core.models import Tweet, SaveTweet
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
            for follow in follows :
                following_users.append(follow.user) # now we have all the following users
            for following_user in following_users:
                tweets = Tweet.objects.filter(user=following_user) | tweets # now we have all the tweets from those users
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
    queryset = Tweet.objects.filter(date_created__gte=yesterday) # Show the tweets from the last 24 hours


class BookMarksView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = SaveTweetSerializer

    def get_queryset(self):
        return SaveTweet.objects.filter(user=self.request.user) # Returns all the savetweet objects


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
        