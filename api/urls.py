from django.urls import path
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [
    path('', views.SignUpView.as_view(), name='signup'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('home', views.HomePageView.as_view(), name='homepage'),
    path('explore', views.ExploreView.as_view(), name='explore'),
    # path('notifications', views.NotificationsView.as_view(), name='notifications'),
    # path('messages', views.MessagesView.as_view(), name='messages')  # Chat App
    path('bookmarks', views.BookMarksView.as_view(), name='bookmarks'),
    path('profiles/<str:username>', views.ProfileView.as_view(), name='profile'),
    # # path('<str:username>/lists', views.ListsView.as_view(), name='lists'),
    path('compose/tweet', views.AddTweetView.as_view(), name='add_tweet'),
]
