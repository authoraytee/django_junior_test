from django.urls import path
 
from .views import EventListView, EventViewSet, EventDetail, EventCreate, EventUpdate, EventDelete

urlpatterns = [
    path('', EventListView.as_view(), name='home'),
    path('events_api/', EventViewSet.as_view({'get': 'list'}), name='events_api'),
    path('event/<int:pk>', EventDetail.as_view(), name='event_detail'),
    path('create', EventCreate.as_view(), name='event_create'),
    path('update/<int:pk>', EventUpdate.as_view(), name='event_update'),
    path('delete/<int:pk>', EventDelete.as_view(), name='event_delete'),
]

