from django.db import models
from django.db.models import Model

import datetime

class Event(Model):
    #PublicationDate = models.DateField()
    EventName = models.CharField(max_length=50)
    PublicationDate = models.DateField(auto_now_add=True, blank=True)
    EventDate = models.DateField(default=datetime.date.today)

    '''
    def clean_EventDate(self, value):
        if value < datetime.datetime.today:
            raise Model.ValidationError('The date must be ...')
        return value
    '''


