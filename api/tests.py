from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from core.models import Tweet, SaveTweet


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


class TestBookMarksView(APITestCase):
    def setUp(self):
        self.new_user = get_user_model().objects.create_user(email='test_user@gmail.com', username='test_username',
                                                             firstname='test_firstname', lastname='test_lastname', password='testpassword', is_active=True)
        self.new_user.refresh_from_db()

    def test_book_mark_endpoint_not_allowed(self):
        """Test not authenticated users can't have access to this endpoint"""
        response = self.client.get(reverse('bookmarks'))
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
            reverse('bookmarks'), **{'HTTP_AUTHORIZATION': f'JWT {access_token}'})

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
