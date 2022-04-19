from django.db import models
from django.contrib.auth import get_user_model


class Tweet(models.Model):
    content = models.CharField(max_length=300)
    date_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name='tweets')


class Like(models.Model):
    tweet = models.ForeignKey(
        Tweet, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name='likes')

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'tweet'], name='Can\'t like same the post twice'
            )
        ]


class Reply(models.Model):
    text = models.TextField(max_length=200)
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name='replies')
    tweet = models.ForeignKey(
        Tweet, on_delete=models.CASCADE, related_name='replies')


# class Retweet()

class SaveTweet(models.Model):
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name='saved_tweets')
    tweet = models.ForeignKey(
        Tweet, on_delete=models.CASCADE, related_name='saved_tweets')

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'tweet'], name='You can\'t save the same post more than once'),
        ]
