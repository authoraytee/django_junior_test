from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from django.shortcuts import render

from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from .models import Event
from .serializers import EventsSerializer


def HomePage(request):

    return render(request, 'home.html')


class EventViewSet(ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=request.user)

class EventDetail(DetailView):
    permission_classes = [IsAuthenticated]

    model = Event
    template_name = 'event_detail.html'

class EventCreate(CreateView):
    permission_classes = [IsAuthenticated]

    model = Event
    template_name = 'event_create.html'
    fields = ('EventName', 'EventDate',)
    success_url = reverse_lazy('home')


class EventUpdate(UpdateView):
    model = Event
    template_name = 'event_update.html'
    context_object_name = 'event'
    fields = ('EventName', 'PublicationDate', 'EventDate',)
    def get_success_url(self):
        return reverse_lazy('event_detail', kwargs={'pk': self.object.id})


class EventDelete(DeleteView):
    model = Event
    template_name = 'event_confirm_delete.html'
    success_url = reverse_lazy('home')