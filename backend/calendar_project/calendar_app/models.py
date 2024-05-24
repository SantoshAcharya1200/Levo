
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .tasks import send_event_notification

class Event(models.Model):
    title = models.CharField(max_length=200)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    description = models.TextField()
    participants = models.ManyToManyField(User,blank=True)
    timezone = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
   
class Notification(models.Model):
    event = models.OneToOneField(Event, on_delete=models.CASCADE)
    is_sent = models.BooleanField(default=False)

@receiver(post_save, sender=Event)
def schedule_notification(sender, instance, created, **kwargs):
    if created:
        send_event_notification.apply_async((instance.id,), eta=instance.start_time)