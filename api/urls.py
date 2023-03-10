from django.urls import path
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [
    path('', views.SignUpView.as_view(), name='signup'),
    path('verify-email/', views.VerifyEmail.as_view(), name='verify-email'),
    path('token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('home', views.HomePageView.as_view(), name='homepage'),
    path('search-tweets/', views.TweetListSearchResults.as_view(), name='search'),
    path('search-users/', views.UserListSearchResults.as_view(), name='search'),
    path('explore', views.ExploreView.as_view(), name='explore'),
    # path('notifications', views.NotificationsView.as_view(), name='notifications'),
    # path('messages', views.MessagesView.as_view(), name='messages')  # Chat App
    path('suggested-users', views.SuggestedUsersView.as_view(), name='suggested-users'),
    path('follow-request/', views.UserFollowView.as_view(), name='user-follow'),
    path('profiles/<int:pk>/follow/delete', views.UserUnfollowWithIdView.as_view(), name='user-unfollow-with-follow-obj-id'),
    path('unfollow/<str:username>', views.UserUnfollowWithUsernameView.as_view(), name='user-unfollow-with-username'),
    path('profiles/<str:username>', views.ProfileDetailView.as_view(), name='profile'),
    path('follow/<str:username>/check', views.FollowCheckView.as_view(), name='follow-check'),
    path('profiles/<str:username>/followers', views.FollowersListView.as_view(), name='followers'),
    path('profiles/<str:username>/followings', views.FollowingsListView.as_view(), name='followings'),
    path('profiles/<str:username>/tweets', views.TweetListView.as_view(), name='tweet-list'),
    path('like-tweet/<int:tweet_id>', views.CreateLikeView.as_view(), name='create-like'),
    path('remove-like/<int:pk>', views.DeleteLikeView.as_view(), name='delete-like'),
    path('list-tweet-likes/<int:tweet_id>', views.ListLikeView.as_view(), name='list-like'),
    path('like/<int:tweet_id>/check', views.LikeCheckView.as_view(), name='like-check'),
    # # path('<str:username>/lists', views.ListsView.as_view(), name='lists'),
    path('compose/tweet', views.AddTweetView.as_view(), name='add_tweet'),
    path('bookmarks', views.BookMarksListView.as_view(), name='bookmarks-list'),
    path('bookmarks/<int:tweet_id>/delete', views.BookMarkDeleteView.as_view(), name='bookmark-delete'),
    path('bookmarks/<int:tweet_id>/check', views.BookMarkCheckView.as_view(), name='bookmark-check'),
    path('tweets/<int:pk>', views.TweetDetailView.as_view(), name='tweet-detail'),
    path('tweets/<int:tweet_id>/create-bookmark', views.BookMarksCreateView.as_view(), name='bookmarks-create'),
    path('tweets/<int:tweet_id>/reply', views.ListCreateReplyView.as_view(), name='list-create-reply'),
    path('check-email/', views.CheckEmailExists.as_view(), name='check-email'),
    path('check-username/', views.CheckUsernameExists.as_view(), name='check-username'),
]
