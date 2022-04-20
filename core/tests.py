from django.test import TestCase
from django.db import IntegrityError
from django.contrib.auth import get_user_model
from .models import Tweet, Like, Reply, SaveTweet


class TestTweet(TestCase):
    def setUp(self):
        self.new_user = get_user_model().objects.create_user(email='test@gmail.com', username='test_username',
                                                             firstname='test_firstname', lastname='test_lastname', password='test_password')

        self.tweet = Tweet.objects.create(
            content='some test', user=self.new_user)

    def test_new_tweet_exists(self):
        """Test new tweet was created with the required fields"""
        self.assertIsInstance(self.tweet, Tweet)

    def test_new_tweet_not_created_without_user(self):
        """Test creating a new tweet is not possible without user"""
        with self.assertRaises(IntegrityError):
            Tweet.objects.create(content='some test')


class TestLike(TestCase):
    def setUp(self):
        self.new_user = get_user_model().objects.create_user(email='test@gmail.com', username='test_username',
                                                             firstname='test_firstname', lastname='test_lastname', password='test_password')
        self.tweet = Tweet.objects.create(
            content='some test', user=self.new_user)
        self.like = Like.objects.create(user=self.new_user, tweet=self.tweet)

    def test_new_like_exists(self):
        """Test user liked the tweet"""
        self.assertIsInstance(self.like, Like)

    def test_cant_like_more(self):
        """Test a user can't like the same tweet more than once"""
        with self.assertRaises(IntegrityError):
            Like.objects.create(user=self.new_user, tweet=self.tweet)

    def test_cant_create_like_without_tweet(self):
        """Test creating a new like is not possible without a tweet object"""
        with self.assertRaises(IntegrityError):
            Like.objects.create(user=self.new_user)

    def test_cant_create_like_without_user(self):
        """Test creating a new like is not possible without a user object"""
        with self.assertRaises(IntegrityError):
            Like.objects.create(tweet=self.tweet)


class TestReply(TestCase):
    def setUp(self):
        self.new_user = get_user_model().objects.create_user(email='test@gmail.com', username='test_username',
                                                             firstname='test_firstname', lastname='test_lastname', password='test_password')

        self.tweet = Tweet.objects.create(
            content='some test', user=self.new_user)

        self.reply = Reply.objects.create(
            text='some test', user=self.new_user, tweet=self.tweet)

    def test_new_reply_exists(self):
        """Test user successfully replied to the tweet"""
        self.assertIsInstance(self.reply, Reply)

    def test_cant_create_reply_without_tweet(self):
        """Test creating a new reply is not possible without a tweet object"""
        with self.assertRaises(IntegrityError):
            Reply.objects.create(text='new test', user=self.new_user)

    def test_cant_create_reply_without_user(self):
        """Test creating a new reply is not possible without a user object"""
        with self.assertRaises(IntegrityError):
            Reply.objects.create(text='new test', tweet=self.tweet)


class TestSaveTweet(TestCase):
    def setUp(self):
        self.new_user = get_user_model().objects.create_user(email='test@gmail.com', username='test_username',
                                                             firstname='test_firstname', lastname='test_lastname', password='test_password')
        self.tweet = Tweet.objects.create(
            content='some test', user=self.new_user)
        self.save_tweet = SaveTweet.objects.create(
            user=self.new_user, tweet=self.tweet)

    def test_new_save_tweet_exists(self):
        """Test user successfully saved the tweet"""
        self.assertIsInstance(self.save_tweet, SaveTweet)

    def test_cant_create_save_tweet_without_tweet(self):
        """Test creating a new save tweet object is not possible without a tweet object"""
        with self.assertRaises(IntegrityError):
            SaveTweet.objects.create(user=self.new_user)

    def test_cant_create_save_tweet_without_user(self):
        """Test creating a new save tweet object is not possible without a user object"""
        with self.assertRaises(IntegrityError):
            SaveTweet.objects.create(tweet=self.tweet)

    def test_cant_create_similar_save_tweet(self):
        """Test integrity error for trying to create an already existing save tweet object"""
        with self.assertRaises(IntegrityError):
            SaveTweet.objects.create(user=self.new_user, tweet=self.tweet)
