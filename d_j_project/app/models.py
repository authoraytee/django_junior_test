from django.db import models
from django.db.models import Model
from django.contrib.auth.models import User
import datetime

class Event(Model):
    EventName = models.CharField(max_length=50)
    PublicationDate = models.DateField(auto_now_add=True, blank=True)
    EventDate = models.DateField(default=datetime.date.today)

    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    '''
    def clean_EventDate(self, value):
        if value < datetime.datetime.today:
            raise Model.ValidationError('The date must be ...')
        return value
    '''