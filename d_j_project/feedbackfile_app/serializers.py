from rest_framework.serializers import ModelSerializer

from feedbackfile_app.models import FileFeedbackEvent

class EventsSerializer(ModelSerializer):
    class Meta:
        model = FileFeedbackEvent
        fields = "__all__"
