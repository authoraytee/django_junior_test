from django.urls import path
 
from .views import index, EventViewSet, EventDetail, EventCreate, EventUpdate, EventDelete

urlpatterns = [
    path('', index, name='index'),
    path('events_api/', EventViewSet.as_view({'get': 'list'}), name='events_api'),
    path('event/<int:pk>', EventDetail.as_view(), name='event_detail'),
    path('create', EventCreate.as_view(), name='event_create'),
    path('update/<int:pk>', EventUpdate.as_view(), name='event_update'),
    path('delete/<int:pk>', EventDelete.as_view(), name='event_delete'),
]

