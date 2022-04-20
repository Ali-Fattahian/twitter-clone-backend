from django.test import TestCase
from django.contrib.auth import get_user_model
from django.db import IntegrityError
from .models import Follow


class TestNewSuperUser(TestCase):
    def setUp(self):
        self.new_super_user = get_user_model().objects.create_superuser(email='test@gmail.com', username='test_username',
                                                                        firstname='test_firstname', lastname='test_lastname', password='test_password')

    def test_new_super_user_exist(self):
        """Test if the new superuser was created"""
        self.assertTrue(self.new_super_user.is_superuser)
        self.assertTrue(self.new_super_user.is_active)
        self.assertTrue(self.new_super_user.is_staff)
        # These three should be set to true for superusers.

    def test_new_super_user_info(self):
        """Test the superuser entered personal information"""
        self.assertEqual(self.new_super_user.email, 'test@gmail.com')
        self.assertEqual(self.new_super_user.username, 'test_username')
        self.assertEqual(self.new_super_user.firstname, 'test_firstname')
        self.assertEqual(self.new_super_user.lastname, 'test_lastname')

    def test_getting_errors(self):
        """Test for getting a ValueError if is_staff or is_superuser is not True"""

        with self.assertRaises(ValueError):
            self.new_super_user = get_user_model().objects.create_superuser(email='test2@gmail.com', username='test_username2',
                                                                            firstname='test_firstname2', lastname='test_lastname2', password='test_password2', is_staff=False)

        with self.assertRaises(ValueError):
            self.new_super_user = get_user_model().objects.create_superuser(email='test2@gmail.com', username='test_username2',
                                                                            firstname='test_firstname2', lastname='test_lastname2', password='test_password2', is_superuser=False)


class TestNewCustomUser(TestCase):
    def setUp(self):
        self.new_user = get_user_model().objects.create_user(email='test@gmail.com', username='test_username',
                                                             firstname='test_firstname', lastname='test_lastname', password='test_password')

    def test_new_user_created(self):
        """Test the new user was successfully created"""
        self.assertIsInstance(self.new_user, get_user_model())

    def test_new_user_not_active(self):
        """Test all those boolean fields are false for a new user"""
        self.assertFalse(self.new_user.is_superuser)
        self.assertFalse(self.new_user.is_active)
        self.assertFalse(self.new_user.is_staff)

    def test_new_super_user_info(self):
        """Test the superuser entered personal information"""
        self.assertEqual(self.new_user.email, 'test@gmail.com')
        self.assertEqual(self.new_user.username, 'test_username')
        self.assertEqual(self.new_user.firstname, 'test_firstname')
        self.assertEqual(self.new_user.lastname, 'test_lastname')

    def test_getting_errors(self):
        """Test for getting a ValueError if the required information was not provided"""

        with self.assertRaises(ValueError):
            self.new_super_user = get_user_model().objects.create_superuser(email='', username='test_username2',
                                                                            firstname='test_firstname2', lastname='test_lastname2', password='test_password2')

        with self.assertRaises(ValueError):
            self.new_super_user = get_user_model().objects.create_superuser(email='test2@gmail.com', username='',
                                                                            firstname='test_firstname2', lastname='test_lastname2', password='test_password2')

        with self.assertRaises(ValueError):
            self.new_super_user = get_user_model().objects.create_superuser(email='test2@gmail.com', username='test_username2',
                                                                            firstname='', lastname='test_lastname2', password='test_password2')

        with self.assertRaises(ValueError):
            self.new_super_user = get_user_model().objects.create_superuser(email='test2@gmail.com', username='test_username2',
                                                                            firstname='test_firstname2', lastname='', password='test_password2')

        with self.assertRaises(ValueError):
            self.new_super_user = get_user_model().objects.create_superuser(email='test2@gmail.com', username='test_username2',
                                                                            firstname='test_firstname2', lastname='test_lastname2', password='')


class TestFollow(TestCase):
    def setUp(self):
        self.new_user1 = get_user_model().objects.create_user(email='test@gmail.com', username='test_username',
                                                              firstname='test_firstname', lastname='test_lastname', password='test_password')
        self.new_user2 = get_user_model().objects.create_user(email='test2@gmail.com', username='test_username2',
                                                              firstname='test_firstname2', lastname='test_lastname2', password='test_password2')

        self.follow1 = Follow.objects.create(
            user=self.new_user1, follower=self.new_user2)
        self.follow2 = Follow.objects.create(
            user=self.new_user2, follower=self.new_user1)

    def test_follow_works(self):
        """Test both users can follow each other"""
        self.assertIsInstance(self.follow1, Follow)
        self.assertIsInstance(self.follow2, Follow)

    def test_same_user_follow_not_valid(self):
        """Test a follow object with the same user for both fields is not possible"""
        with self.assertRaises(IntegrityError):
            Follow.objects.create(user=self.new_user1, follower=self.new_user1)

    def test_same_user_follow_not_valid(self):
        """Test a user can't follow the other user more than once"""
        with self.assertRaises(IntegrityError):
            Follow.objects.create(user=self.new_user1, follower=self.new_user2)        
