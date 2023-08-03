# Twitter Clone Project - Backend

### Description

Server side and API of twitter clone project. This project was build with Django and Django REST Framework. For storing media files, cloudinary service was used,
Users have to provide an email then validate it to sign up to the website.
For the login process, access and refresh token method was used.
For production, a react app is rendered by django as a single html file.

### Features

- Users can create tweets and change or delete them if they want.
- Users can follow each other and see their following user's tweets in home page.
- Users can like tweets, save them and reply to each tweet.
- Users can add bio, background picture, profile picture and their name.
- Users see the creation date of tweets the same way twitter works.
- Users can search the tweets and users separately.
- Users can see every user that liked a tweet.
- An end point for sending suggested users to users.
- For validating email, a different thread is used to speed up the process.
- For creating an account, the frontend applications can use an end point to check live if a username was used before.

### Technologies and libraries used

- Django
- Django REST framework
- Django filters
- Django REST framework simple jwt
- Django cors headers
- Postgres
- psycopg2
- dj-database-url
- Cloudinary
- Django cloudinary storage
- Django white noise
- Pillow
- gunicorn
- python-dotenv

### How to run the project

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/Ali-Fattahian/twitter-clone-backend.git
```

Create a virtual environment to install dependencies in and activate it:

```sh
python3 -m venv env
source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```

Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment.

Since this project is in production, you have to change settings to dev to work with it, so open settings.py,

Use an online tool like *https://djecrety.ir/*
to get a new secret key for the project.

Set DEBUG=True,

Create a database and set DATABASES settings to the one you created,

either remove cloudinary settings and apps from installed_apps or set the configuration to your own account, at last set the email config to your email.

once you did all of that,

```ssh
python manage.py runserver
```

to run the server.

You can navigate to
`http://localhost:8000/api/`
to access the api routes

If you navigate to
`http://localhost:8000`
you access the react app that is working as a single page (index.html) rendered by django.

To run the tests,
`python manage.py tests`
