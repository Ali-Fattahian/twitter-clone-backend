from rest_framework import permissions
from django.core.mail import EmailMessage


# only the user has access to edit-profile page specific to that user
class OnlySameUserCanEditMixin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj == request.user


def datetime_subtractor(new_datetime, old_datetime):
    sub = new_datetime - old_datetime
    total_seconds = sub.total_seconds()
    seconds_for_all_days = (sub.days * 24 * 3600)
    remainder = total_seconds - seconds_for_all_days  # if we don't consider the days
    hours_left_complete = remainder / 3600
    hours_left = int(remainder//3600)  # Hours
    minutes_left_complete = (hours_left_complete -
                             hours_left) * 60  # get the minutes
    # decimal part of the number						Minutes
    minutes_left = int(minutes_left_complete)
    seconds_left_complete = (minutes_left_complete - minutes_left) * 60
    seconds_left = int(seconds_left_complete)  # Seconds

    answer = {}

    if sub.days > 0:
        answer['days'] = sub.days
    else:
        answer['days'] = 0

    if hours_left > 0:
        answer['hours'] = hours_left
    else:
        answer['hours'] = 0

    if minutes_left > 0:
        answer['minutes'] = minutes_left
    else:
        answer['minutes'] = 0

    if seconds_left > 0:
        answer['seconds'] = seconds_left
    else:
        answer['seconds'] = 0

    return answer


class EmailRelatedClass:
    @staticmethod
    def send_email(data):
        email = EmailMessage(
            subject=data['email_subject'], body=data['email_body'], to=[data['to_email']])

        email.send()
