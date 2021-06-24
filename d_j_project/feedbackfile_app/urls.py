from django.urls import path
 
from .views import SendFileFeedback, FileFeedbackEventListView, FileFeedbackEventDetail, FileFeedbackEventCreate, FileFeedbackEventUpdate, FileFeedbackEventDelete, SendFeedback, EventSubscribe

urlpatterns = [
    path('filefeedback_events_home/', FileFeedbackEventListView.as_view(), name='filefeedback_events_home'),

    path('filefeedback_event/<int:pk>', FileFeedbackEventDetail.as_view(), name='filefeedback_event_detail'),
    path('filefeedback_create/', FileFeedbackEventCreate.as_view(), name='filefeedback_event_create'),
    path('filefeedback_update/<int:pk>', FileFeedbackEventUpdate.as_view(), name='filefeedback_event_update'),
    path('filefeedback_delete/<int:pk>', FileFeedbackEventDelete.as_view(), name='filefeedback_event_delete'),

    path('send_feedback_file/<int:event>', SendFileFeedback.as_view(), name='filefeedback_send_feedback_file'),
    path('send_feedback/<int:event>', SendFeedback.as_view(), name='filefeedback_send_feedback'),
    path('subscribe/<int:event>', EventSubscribe, name='filefeedback_subscribe_event'),
]

