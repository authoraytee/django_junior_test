from django.contrib import admin

from .models import FileFeedbackEvent, FileFeedbackEventToSubscriber

admin.site.register(FileFeedbackEvent)
admin.site.register(FileFeedbackEventToSubscriber)

