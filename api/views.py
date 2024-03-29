from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, filters, status
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
# from datetime import datetime, timedelta, timezone
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
import jwt
from django.conf import settings
from django.contrib.auth.hashers import make_password
import threading

from .serializers import LikeSerializer, UserSignUpSerializer, TweetSerializer, SaveTweetSerializer, ProfileSerializer, FollowSerializer, ReplySerializer
from core.models import Tweet, SaveTweet, Like, Reply
from users.models import Follow
from .utils import OnlySameUserCanEditMixin, EmailRelatedClass


class EmailThreading(threading.Thread):
    def __init__(self, data) :
        self.email = data
        threading.Thread.__init__(self)
    
    def run(self):
        EmailRelatedClass.send_email(self.email)


class SignUpView(generics.GenericAPIView):
    serializer_class = UserSignUpSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['password'] = make_password(serializer.validated_data['password'])
        serializer.save()
        user = get_object_or_404(
            get_user_model(), email=serializer.data.get('email'))
        token = RefreshToken.for_user(user).access_token
        current_site = get_current_site(request).domain
        # relative_link = reverse('verify-email')
        absolute_url = f'https://{current_site}/#/activate-account/{token}'
        email_body = f'Hi {user.username}, Welcome to Twitter Clone, Please use the link below to verify your email.\n{absolute_url}'

        data = {'email_body': email_body,
                'email_subject': 'Verify your email', 'to_email': user.email}
        EmailThreading(data).start()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class VerifyEmail(generics.GenericAPIView):
    def get(self, request):
        token = request.GET.get('token')
        try:
            payload = jwt.decode(
                token, settings.SECRET_KEY, algorithms='HS256')
            user = get_object_or_404(get_user_model(), id=payload['user_id'])
            if not user.is_active:
                user.is_active = True
                user.save()
            return Response({'email': 'Successfully activated'}, status=status.HTTP_200_OK)
        except jwt.ExpiredSignatureError:
            return Response({'error': 'Activation expired'}, status=status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError:
            return Response({'error: Invalid token'}, status=status.HTTP_400_BAD_REQUEST)

    
class CheckEmailExists(generics.GenericAPIView):
    def post(self, request):
        email = request.data.get('email')
        if get_user_model().objects.filter(email=email).exists():
            return Response(True, status=status.HTTP_200_OK)
        return Response(False, status=status.HTTP_200_OK)


class CheckUsernameExists(generics.GenericAPIView):
    def post(self, request):
        username = request.data.get('username')
        if get_user_model().objects.filter(username=username).exists():
            return Response(True, status=status.HTTP_200_OK)
        return Response(False, status=status.HTTP_200_OK)


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
    # now = datetime.now(timezone.utc)
    # yesterday = now - timedelta(days=1)
    # queryset = Tweet.objects.filter(date_created__gte=yesterday) # Show the tweets from the last 24 hours -- not worth it for a small website
    queryset = Tweet.objects.all().order_by('-date_created')[:20]


class BookMarksListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = SaveTweetSerializer

    def get_queryset(self):
        # Returns all the savetweet objects
        return SaveTweet.objects.filter(user=self.request.user)


class BookMarksCreateView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = SaveTweetSerializer

    def perform_create(self, serializer):
        tweet = get_object_or_404(Tweet, id=self.kwargs.get('tweet_id'))
        serializer.save(user=self.request.user, tweet=tweet)


class BookMarkDeleteView(generics.DestroyAPIView):
    queryset = SaveTweet.objects.all()
    serializer_class = SaveTweetSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        tweet = get_object_or_404(Tweet, id=self.kwargs.get('tweet_id'))
        return get_object_or_404(SaveTweet, tweet=tweet, user=self.request.user)

    def perform_destroy(self, instance):
        if instance.user == self.request.user:
            return super().perform_destroy(instance)
        return Response(status.HTTP_401_UNAUTHORIZED)


class BookMarkCheckView(generics.RetrieveAPIView):
    queryset = SaveTweet.objects.all()
    serializer_class = SaveTweetSerializer

    def get_object(self):
        tweet = get_object_or_404(Tweet, id=self.kwargs.get('tweet_id'))
        return get_object_or_404(SaveTweet, tweet=tweet, user=self.request.user)



class SuggestedUsersView(generics.ListAPIView):
    serializer_class = ProfileSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            followings = []
            followings.append(self.request.user.username)
            follow_objs = Follow.objects.filter(follower=self.request.user)
            for follow_obj in follow_objs:
                followings.append(follow_obj.user.username)
            suggested_users = get_user_model().objects.exclude(username__in=followings).exclude(is_active=False)
            if len(suggested_users) >3:
                return suggested_users[:3]
            return suggested_users
        return get_user_model().objects.all()[:3]


class UserFollowView(generics.CreateAPIView):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(follower=self.request.user)


class UserUnfollowWithIdView(generics.DestroyAPIView):
    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Follow.objects.filter(follower=self.request.user)


class UserUnfollowWithUsernameView(generics.DestroyAPIView):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        following_user = get_object_or_404(get_user_model(), username=self.kwargs.get('username'))
        print(following_user)
        return get_object_or_404(Follow, user=following_user, follower=self.request.user)


class FollowCheckView(generics.RetrieveAPIView):
    queryset = Follow.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FollowSerializer

    def get_object(self):
        following_username = self.kwargs.get('username')
        following_user = get_object_or_404(
            get_user_model(), username=following_username)
        return get_object_or_404(Follow, user=following_user, follower=self.request.user)


class ProfileDetailView(generics.RetrieveUpdateAPIView):
    queryset = get_user_model().objects.all()
    permission_classes = [OnlySameUserCanEditMixin]
    serializer_class = ProfileSerializer
    lookup_field = 'username'

    def perform_update(self, serializer):
        instance = self.get_object()
        password = self.request.data.get('password', None)
        if password:
            if len(password) < 8:
                raise ValidationError(
                    {'detail': 'Password can\'t be less than 8 characters long'})
            instance.set_password(password)
            instance.save()


class TweetListView(generics.ListAPIView):
    serializer_class = TweetSerializer

    def get_queryset(self):
        user = get_object_or_404(
            get_user_model(), username=self.kwargs.get('username'))
        return Tweet.objects.filter(user=user)


class TweetDetailView(generics.RetrieveAPIView):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer


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
        return Response(status.HTTP_401_UNAUTHORIZED)


class ListLikeView(generics.ListAPIView):
    serializer_class = LikeSerializer

    def get_queryset(self):
        tweet = get_object_or_404(Tweet, id=self.kwargs.get('tweet_id'))
        return Like.objects.filter(tweet=tweet)


class LikeCheckView(generics.RetrieveAPIView):
    queryset = Like.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = LikeSerializer

    def get_object(self):
        tweet_id = self.kwargs.get('tweet_id')
        tweet = get_object_or_404(Tweet, id=tweet_id)
        return get_object_or_404(Like, user=self.request.user, tweet=tweet)


class ListCreateReplyView(generics.ListCreateAPIView):
    serializer_class = ReplySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        tweet = get_object_or_404(Tweet, id=self.kwargs.get('tweet_id'))
        return Reply.objects.filter(tweet=tweet)

    def perform_create(self, serializer):
        tweet = get_object_or_404(Tweet, id=self.kwargs.get('tweet_id'))
        serializer.save(user=self.request.user, tweet=tweet)


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['username'] = user.username
        # ...

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
