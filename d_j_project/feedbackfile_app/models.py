from django.db import models
from django.db.models import Model
from django.contrib.auth.models import User

import datetime

from django.db.models.fields import CharField

class FileFeedbackEvent(Model):
    EventName = models.CharField(max_length=50)
    EventType = "File-Feedback-Event"
    PublicationDate = models.DateField(auto_now_add=True, blank=True)
    EventDate = models.DateField(default=datetime.date.today)

    owner = models.ForeignKey(User, on_delete = models.CASCADE, related_name="FileFeedbackOwner", verbose_name='Владелец события', blank = True, null = True)

    def __str__(self):
        return self.EventName

        
class FileFeedbackEventToSubscriber(Model):
    event = models.ManyToManyField(FileFeedbackEvent, verbose_name='Событие')
    subscriber = models.ManyToManyField(User, verbose_name='Подписчик')
    feedback = CharField(max_length=1000, null=True)
    FeedbackFile = models.FileField(upload_to='files/', null=True, blank=True)
    SubscriptionDate = models.DateField(default=datetime.date.today)
