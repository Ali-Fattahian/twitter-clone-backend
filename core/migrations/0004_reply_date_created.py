# Generated by Django 4.0 on 2022-05-15 15:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_tweet_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='reply',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
