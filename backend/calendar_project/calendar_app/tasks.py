from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_event_notification(email):
    send_mail(
        'Event Notification',
        f'You have an upcoming event:',
        'rmsportquiz@gmail.com',
        [email],
        fail_silently=False,
    )