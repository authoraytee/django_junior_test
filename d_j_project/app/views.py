from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


from .models import Event
 
#@method_decorator(login_required, name='dispatch')

class EventList(ListView):
    model = Event
    template_name = 'home.html'


class EventDetail(DetailView):
    model = Event
    template_name = 'event_detail.html'

class EventCreate(CreateView):
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