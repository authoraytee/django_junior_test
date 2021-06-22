from django.db import models
from django.db.models import Model
from django.contrib.auth.models import User, Group
import datetime

class Event(Model):
    EventName = models.CharField(max_length=50)
    PublicationDate = models.DateField(auto_now_add=True, blank=True)
    EventDate = models.DateField(default=datetime.date.today)

    owner = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name='Владелец события', blank = True, null = True )

    def __str__(self):
        return self.EventName
        
