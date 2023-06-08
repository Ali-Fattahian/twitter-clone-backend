from django.db import models
from django.contrib.auth import get_user_model


class Tweet(models.Model):
    content = models.TextField(max_length=300) #Make this required on the view
    date_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name='tweets')

    @property
    def get_likes(self):
        return self.likes.all().count()
    
    def __str__(self):
        return f'tweet {self.id} by {self.user.username}'


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

    def __str__(self):
        return f'{self.user.username} liked tweet {self.tweet.id} by {self.tweet.user.username}'


class Reply(models.Model):
    text = models.TextField(max_length=200) #Make this required on the view
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name='replies')
    tweet = models.ForeignKey(
        Tweet, on_delete=models.CASCADE, related_name='replies')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'reply to {self.tweet.user.username}\'s tweet by {self.user.username}'

    class Meta:
        ordering = ['-id']
        verbose_name_plural = 'Replies'

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
        verbose_name_plural = 'Save Tweets'

    def __str__(self):
        return f'{self.user.username} saved {self.tweet.id} tweet by {self.tweet.user.username}'
