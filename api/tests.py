from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from core.models import Tweet, SaveTweet
from users.models import Follow


class TestSignUpView(APITestCase):
    def test_create_user(self):
        """Test user creation is successful"""
        response = self.client.post(reverse('signup'), data={
            'email': 'test_user@gmail.com',
            'username': 'test_username',
            'firstname': 'test_firstnamse',
            'lastname': 'test_lastname',
            'password': 'testpassword'
        })
        self.assertEqual(response.status_code, 201)

        new_user = get_user_model().objects.filter(
            email='test_user@gmail.com', username='test_username')
        self.assertTrue(new_user)

    def test_not_create_user(self):
        """Test user creation fails without providing either of fields"""
        response = self.client.post(reverse('signup'), data={
            'email': 'test_user@gmail.com',
            'username': 'test_username',
            'firstname': 'test_firstnamse',
            'lastname': 'test_lastname'
        })
        self.assertEqual(response.status_code, 400)

        response = self.client.post(reverse('signup'), data={
            'email': 'test_user@gmail.com',
            'username': 'test_username',
            'firstname': 'test_firstnamse',
            'password': 'testpassword'
        })

        self.assertEqual(response.status_code, 400)

        response = self.client.post(reverse('signup'), data={
            'email': 'test_user@gmail.com',
            'username': 'test_username',
            'lastname': 'test_lastname',
            'password': 'testpassword'
        })

        self.assertEqual(response.status_code, 400)

        response = self.client.post(reverse('signup'), data={
            'email': 'test_user@gmail.com',
            'firstname': 'test_firstnamse',
            'lastname': 'test_lastname',
            'password': 'testpassword'
        })

        self.assertEqual(response.status_code, 400)

        response = self.client.post(reverse('signup'), data={
            'username': 'test_username',
            'firstname': 'test_firstnamse',
            'lastname': 'test_lastname',
            'password': 'testpassword'
        })

        self.assertEqual(response.status_code, 400)

    def test_new_user_not_staff_active(self):
        """Test new user is not active and is not staff"""

        self.client.post(reverse('signup'), data={
            'email': 'test_user@gmail.com',
            'username': 'test_username',
            'firstname': 'test_firstnamse',
            'lastname': 'test_lastname',
            'password': 'testpassword'
        })

        new_user = get_user_model().objects.get(email='test_user@gmail.com')
        self.assertFalse(new_user.is_staff)
        self.assertFalse(new_user.is_active)


class TestHomePageView(APITestCase):
    def setUp(self):
        self.new_user = get_user_model().objects.create_user(email='test_user@gmail.com', username='test_username',
                                                             firstname='test_firstname', lastname='test_lastname', password='testpassword', is_active=True)
        self.new_user.refresh_from_db()

    def test_home_page_works(self):
        """Test home page page loads for all users"""
        response = self.client.get(reverse('homepage'))
        self.assertEqual(response.status_code, 200)

    def test_home_page_not_work_for_post_method(self):
        """Test home page view doesn't allow post method for non-auth users"""
        response = self.client.post(reverse('homepage'), data={
                                    'content': 'new tweet'})
        self.assertEqual(response.status_code, 401)

    def test_home_page_works_for_users(self):
        """Test home page view allow users to add new tweets"""
        response = self.client.post(reverse('token_obtain_pair'), {
                                    'email': 'test_user@gmail.com', 'password': 'testpassword'})
        self.assertEqual(response.status_code, 200)
        access_token = response.data['access']

        homepage_response = self.client.post(reverse('homepage'), {
            'content': 'new tweet'
        }, **{'HTTP_AUTHORIZATION': f'JWT {access_token}'})

        self.assertEqual(homepage_response.status_code, 201)

        new_tweet = Tweet.objects.get(content='new tweet', user=self.new_user)
        self.assertTrue(new_tweet)
        self.assertIsInstance(new_tweet, Tweet)


class TestExploreView(APITestCase):
    def test_explore_view_allow_get(self):
        """Test explore page works for get method"""
        response = self.client.get(reverse('explore'))
        self.assertEqual(response.status_code, 200)

    def test_explore_view_not_allow_post(self):
        """Test explore page doesn't work for post method"""
        response = self.client.post(reverse('explore'))
        self.assertEqual(response.status_code, 405)

    def test_explore_view_show_tweet(self):
        """Test explore view sends the new added tweet"""
        new_user = get_user_model().objects.create_user(email='test_user@gmail.com', username='test_username',
                                                        firstname='test_firstname', lastname='test_lastname', password='testpassword', is_active=True)
        new_tweet = Tweet.objects.create(content='test', user=new_user)
        response = self.client.get(reverse('explore'))
        self.assertTrue(response.data[0].get('id') == new_tweet.id)
        self.assertTrue(response.data[0].get('content') == new_tweet.content)


class TestBookMarksListView(APITestCase):
    def setUp(self):
        self.new_user = get_user_model().objects.create_user(email='test_user@gmail.com', username='test_username',
                                                             firstname='test_firstname', lastname='test_lastname', password='testpassword', is_active=True)
        self.new_user.refresh_from_db()

    def test_book_mark_endpoint_not_allowed(self):
        """Test not authenticated users can't have access to this endpoint"""
        response = self.client.get(reverse('bookmarks-list'))
        self.assertEqual(response.status_code, 401)

    def test_book_mark_endpoint_allowed_and_works(self):
        """Test authenticated users have access to this endpoint and get the right content"""
        response = self.client.post(reverse('token_obtain_pair'), {
                                    'email': 'test_user@gmail.com', 'password': 'testpassword'})
        access_token = response.data['access']

        new_tweet = Tweet.objects.create(content='test', user=self.new_user)
        save_tweet = SaveTweet.objects.create(
            tweet=new_tweet, user=self.new_user)
        book_mark_response = self.client.get(
            reverse('bookmarks-list'), **{'HTTP_AUTHORIZATION': f'JWT {access_token}'})

        self.assertEqual(book_mark_response.status_code, 200)

        self.assertEqual(book_mark_response.data[0].get('id'), save_tweet.id)


class TestProfileView(APITestCase):
    def setUp(self):
        self.new_user = get_user_model().objects.create_user(email='test_user@gmail.com', username='test_username',
                                                             firstname='test_firstname', lastname='test_lastname', password='testpassword', is_active=True)
        self.new_user.refresh_from_db()

    def test_profile_view_works_get(self):
        """Test profile endpoint works for get request for all users"""
        response = self.client.get(
            reverse('profile', args=[self.new_user.username]))
        self.assertEqual(response.status_code, 200)

    def test_profile_view_not_work_post(self):
        """Test profile endpoint doesn't work for not-auth users for post request"""
        response = self.client.patch(
            reverse('profile', args=[self.new_user.username]))
        self.assertEqual(response.status_code, 401)

    def test_profile_view_work_patch(self):
        """Test profile endpoint works for auth users for post request"""
        response = self.client.post(reverse('token_obtain_pair'), {
                                    'email': self.new_user.email, 'password': 'testpassword'})
        access_token = response.data['access']

        profile_response = self.client.patch(reverse('profile', args=[self.new_user.username]), {
                                             'bio': 'new bio'}, **{'HTTP_AUTHORIZATION': f'JWT {access_token}'})
        self.assertEqual(profile_response.status_code, 200)


class TestAddTweetView(APITestCase):
    def setUp(self):
        self.new_user = get_user_model().objects.create_user(email='test_user@gmail.com', username='test_username',
                                                             firstname='test_firstname', lastname='test_lastname', password='testpassword', is_active=True)
        self.new_user.refresh_from_db()

    def test_add_tweet_not_work_for_not_users(self):
        """Test add tweet deosn't work for any request from not-users"""
        get_response = self.client.get(reverse('add_tweet'))
        self.assertEqual(get_response.status_code, 401)

        post_response = self.client.post(reverse('add_tweet'))
        self.assertEqual(post_response.status_code, 401)

    def test_add_tweet_not_work_for_get(self):
        """Test add tweet endpoint doesn't work for get request"""
        response = self.client.post(reverse('token_obtain_pair'), {
                                    'email': self.new_user.email, 'password': 'testpassword'})
        access_token = response.data['access']

        add_tweet_response = self.client.get(
            reverse('add_tweet'), **{'HTTP_AUTHORIZATION': f'JWT {access_token}'})
        self.assertEqual(add_tweet_response.status_code, 405)

    def test_add_tweet_works_for_post(self):
        """Test users can add new post from this endpoint"""
        response = self.client.post(reverse('token_obtain_pair'), {
                                    'email': self.new_user.email, 'password': 'testpassword'})
        access_token = response.data['access']

        add_tweet_response = self.client.post(
            reverse('add_tweet'), {'content': 'new tweet'}, **{'HTTP_AUTHORIZATION': f'JWT {access_token}'})

        self.assertEqual(add_tweet_response.status_code, 201)

        new_tweet = Tweet.objects.get(user=self.new_user, content='new tweet')
        self.assertTrue(new_tweet)
        self.assertIsInstance(new_tweet, Tweet)


class TestTweetDetailView(APITestCase):
    def setUp(self):
        self.new_user = get_user_model().objects.create_user(email='test_user@gmail.com', username='test_username',
                                                             firstname='test_firstname', lastname='test_lastname', password='testpassword', is_active=True)
        self.new_tweet = Tweet.objects.create(
            content='test content', user=self.new_user)

    def test_detail_view_works(self):
        """Test this view works for retrieving an existing tweet"""
        response = self.client.get(
            reverse('tweet-detail', args=[self.new_tweet.pk]))
        self.assertEqual(response.status_code, 200)

    def test_detail_view_404(self):
        """Test this view returns 404 if the tweet id doesn't exist"""
        response = self.client.get(
            reverse('tweet-detail', args=[self.new_tweet.pk+1]))  # A non existing tweet
        self.assertEqual(response.status_code, 404)

    def test_only_get_allowed(self):
        """Test you are not allowed to send anything but a GET request"""
        post_response = self.client.post(
            reverse('tweet-detail', args=[self.new_tweet.pk]))
        delete_response = self.client.delete(
            reverse('tweet-detail', args=[self.new_tweet.pk]))
        put_response = self.client.put(
            reverse('tweet-detail', args=[self.new_tweet.pk]))
        patch_response = self.client.patch(
            reverse('tweet-detail', args=[self.new_tweet.pk]))
        self.assertEqual(post_response.status_code, 405)
        self.assertEqual(delete_response.status_code, 405)
        self.assertEqual(put_response.status_code, 405)
        self.assertEqual(patch_response.status_code, 405)


class TestTweetListView(APITestCase):
    def setUp(self):
        self.new_user = get_user_model().objects.create_user(email='test_user@gmail.com', username='test_username',
                                                             firstname='test_firstname', lastname='test_lastname', password='testpassword', is_active=True)

    def test_tweet_list_ok_response(self):
        """Test this endpoint returns 200 even if there is no tweets"""
        response = self.client.get(
            reverse('tweet-list', args=[self.new_user.username]))
        self.assertEqual(response.status_code, 200)

    def test_tweet_list_get_only(self):
        """Test you are not allowed to send anything but a GET request"""
        post_response = self.client.post(
            reverse('tweet-list', args=[self.new_user.username]))
        delete_response = self.client.delete(
            reverse('tweet-list', args=[self.new_user.username]))
        put_response = self.client.put(
            reverse('tweet-list', args=[self.new_user.username]))
        patch_response = self.client.patch(
            reverse('tweet-list', args=[self.new_user.username]))
        self.assertEqual(post_response.status_code, 405)
        self.assertEqual(delete_response.status_code, 405)
        self.assertEqual(put_response.status_code, 405)
        self.assertEqual(patch_response.status_code, 405)

    def test_new_tweet_returns(self):
        """Test that this endpoint returns the new tweet"""
        new_tweet = Tweet.objects.create(
            content='test content', user=self.new_user)
        response = self.client.get(
            reverse('tweet-list', args=[self.new_user.username]))
        self.assertEqual(response.data[0].get('content'), new_tweet.content)
        self.assertEqual(response.data[0].get('id'), new_tweet.id)


class TestFollowersListView(APITestCase):
    def setUp(self):
        self.new_user1 = get_user_model().objects.create_user(email='test_user1@gmail.com', username='test_username1',
                                                              firstname='test_firstname', lastname='test_lastname', password='testpassword', is_active=True)
        self.new_user2 = get_user_model().objects.create_user(email='test_user2@gmail.com', username='test_username2',
                                                              firstname='test_firstname', lastname='test_lastname', password='testpassword', is_active=True)

    def test_followers_list_ok_response(self):
        """Test this endpoint returns 200 even if there is no tweets"""
        response = self.client.get(
            reverse('followers', args=[self.new_user1.username]))
        self.assertEqual(response.status_code, 200)

    def test_followers_list_get_only(self):
        """Test you are not allowed to send anything but a GET request"""
        post_response = self.client.post(
            reverse('followers', args=[self.new_user1.username]))
        delete_response = self.client.delete(
            reverse('followers', args=[self.new_user1.username]))
        put_response = self.client.put(
            reverse('followers', args=[self.new_user1.username]))
        patch_response = self.client.patch(
            reverse('followers', args=[self.new_user1.username]))
        self.assertEqual(post_response.status_code, 405)
        self.assertEqual(delete_response.status_code, 405)
        self.assertEqual(put_response.status_code, 405)
        self.assertEqual(patch_response.status_code, 405)

    def test_new_follow_object_returns(self):
        """Test this endpoint returns the new created follow object"""
        new_follow = Follow.objects.create(
            user=self.new_user1, follower=self.new_user2)
        response = self.client.get(
            reverse('followers', args=[self.new_user1.username]))
        self.assertEqual(response.data[0].get(
            'username'), new_follow.follower.username)
        self.assertEqual(response.data[0].get(
            'email'), new_follow.follower.email)


class TestFollowingsListView(APITestCase):
    def setUp(self):
        self.new_user1 = get_user_model().objects.create_user(email='test_user1@gmail.com', username='test_username1',
                                                              firstname='test_firstname', lastname='test_lastname', password='testpassword', is_active=True)
        self.new_user2 = get_user_model().objects.create_user(email='test_user2@gmail.com', username='test_username2',
                                                              firstname='test_firstname', lastname='test_lastname', password='testpassword', is_active=True)

    def test_followings_list_ok_response(self):
        """Test this endpoint returns 200 even if there is no tweets"""
        response = self.client.get(
            reverse('followings', args=[self.new_user2.username]))
        self.assertEqual(response.status_code, 200)

    def test_followings_list_get_only(self):
        """Test you are not allowed to send anything but a GET request"""
        post_response = self.client.post(
            reverse('followings', args=[self.new_user2.username]))
        delete_response = self.client.delete(
            reverse('followings', args=[self.new_user2.username]))
        put_response = self.client.put(
            reverse('followings', args=[self.new_user2.username]))
        patch_response = self.client.patch(
            reverse('followings', args=[self.new_user2.username]))
        self.assertEqual(post_response.status_code, 405)
        self.assertEqual(delete_response.status_code, 405)
        self.assertEqual(put_response.status_code, 405)
        self.assertEqual(patch_response.status_code, 405)

    def test_new_follow_object_returns(self):
        """Test this endpoint returns the new created follow object"""
        new_follow = Follow.objects.create(
            user=self.new_user1, follower=self.new_user2)
        response = self.client.get(
            reverse('followings', args=[self.new_user2.username]))
        self.assertEqual(response.data[0].get(
            'username'), new_follow.user.username)
        self.assertEqual(response.data[0].get(
            'email'), new_follow.user.email)
