from django.urls import path
 
from .views import EventListView, EventDetail, EventCreate, EventUpdate, EventDelete, EventSubscribe#, EventUnSubscribe

urlpatterns = [
    path('', EventListView.as_view(), name='home'),
    
    path('event/<int:pk>', EventDetail.as_view(), name='event_detail'),
    path('event/create', EventCreate.as_view(), name='event_create'),
    path('event/update/<int:pk>', EventUpdate.as_view(), name='event_update'),
    path('event/delete/<int:pk>', EventDelete.as_view(), name='event_delete'),

    path('subscribe/<int:event>', EventSubscribe, name='event_subscribe'),
    # path('unsub/<int:event>', EventUnSubscribe, name='event_un_subscribe'),

]

