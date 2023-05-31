from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomAccountManager(BaseUserManager):
    def create_superuser(self, email, username, firstname, lastname, password, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        kwargs.setdefault('is_active', True)

        if kwargs.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned to is_staff=True')

        if kwargs.get('is_superuser') is not True:
            raise ValueError('Superuser must be assigned to is_superuser=True')

        return self.create_user(email, username, firstname, lastname, password, **kwargs)

    def create_user(self, email, username, firstname, lastname, password, **kwargs):
        required_fields = (email, username, firstname, lastname, password)

        # All of the fields should be provided(True)
        if not (email and username and firstname and lastname and password):
            raise ValueError(_('The fields must not be empty.'))

        email = self.normalize_email(email)
        user = self.model(email=email, username=username,
                          firstname=firstname, lastname=lastname, **kwargs)
        user.set_password(password)
        user.save()
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(max_length=150, unique=True)
    firstname = models.CharField(max_length=150)
    lastname = models.CharField(max_length=150)
    join_date = models.DateTimeField(auto_now_add=True)
    bio = models.TextField(_('bio'), max_length=255, blank=True, default='')
    picture = models.ImageField(
        blank=True, default='profile_pictures/default_profile.png')
    background_picture = models.ImageField(blank=True, default='profile_pictures/default_background_picture.png')
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = CustomAccountManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'firstname', 'lastname']

    def __str__(self):
        return f'Username: {self.username} | Email: {self.email}'

    class Meta(AbstractBaseUser.Meta):
        verbose_name_plural = 'Users'
        verbose_name = 'User'


class Follow(models.Model):
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name='followers')
    follower = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name='follows')

    class Meta:
        constraints = [
            models.CheckConstraint(check=~models.Q(user=models.F(
                'follower')), name='user and follower fields can not be the same.'),
            models.UniqueConstraint(fields=[
                                    'user', 'follower'], name='Can\'t follow the same user more than once')
        ]

    def __str__(self):
        return f'User {self.follower.username} followed {self.user.username}'
