from datetime import datetime, timedelta

import pytz

from config import settings
from django.core.mail import send_mail
from celery import shared_task

from materials.models import Course, Subscription
from users.models import User


@shared_task
def add_mail(course_id):
    course = Course.objects.get(pk=course_id)
    subscribers = Subscription.objects.get(courses=course_id)

    send_mail(
        subject=f"Курс {course} обновлен",
        message=f"Курс {course},на который вы подписаны обновлён",
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[subscribers.owner.email],
    )


@shared_task
def check_activity():
    """блокировка неактивных пользователей"""
    zone = pytz.timezone(settings.TIME_ZONE)
    now = datetime.now(zone)
    active_users = User.objects.filter(is_active=True)
    for user in active_users:
        if user.last_login:
            if now - user.last_login > timedelta(days=30):
                user.is_active = False
                user.save()
