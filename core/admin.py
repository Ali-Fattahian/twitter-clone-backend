from django.contrib import admin
from .models import Tweet, Like, Reply, SaveTweet

admin.site.register(Tweet)
admin.site.register(Like)
admin.site.register(Reply)
admin.site.register(SaveTweet)
