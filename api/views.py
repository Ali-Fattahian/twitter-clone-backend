from rest_framework import generics, permissions
from django.contrib.auth import get_user_model
from .serializers import CustomUserSerializer, TweetSerializer
from core.models import Tweet
from users.models import Follow


class SignUpView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = CustomUserSerializer


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
            return tweets
        return Tweet.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)            