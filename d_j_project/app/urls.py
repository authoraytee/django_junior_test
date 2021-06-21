from django.urls import path
 
from .views import HomePage, EventViewSet, EventDetail, EventCreate, EventUpdate, EventDelete

urlpatterns = [
    path('', HomePage, name="home"),
    path('event/<int:pk>', EventDetail.as_view(), name='event_detail'),
    path('create', EventCreate.as_view(), name='event_create'),
    path('update/<int:pk>', EventUpdate.as_view(), name='event_update'),
    path('delete/<int:pk>', EventDelete.as_view(), name='event_delete'),
]

'''
urlpatterns = [
    path('event/<int:pk>', EventDetail.as_view(), name='event_detail'),
    path('create', EventCreate.as_view(), name='event_create'),
    path('update/<int:pk>', EventUpdate.as_view(), name='event_update'),
    path('delete/<int:pk>', EventDelete.as_view(), name='event_delete'),
    path('', EventList.as_view(), name='home'),
]
'''