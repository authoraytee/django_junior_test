from .models import FileFeedbackEventToSubscriber
from django.forms import ModelForm

class FileFieldForm(ModelForm):
    class Meta:
        model = FileFeedbackEventToSubscriber
        fields = ('FeedbackFile',)

class FeedbackForm(ModelForm):
    class Meta:
        model = FileFeedbackEventToSubscriber
        fields = ('feedback',)
    
