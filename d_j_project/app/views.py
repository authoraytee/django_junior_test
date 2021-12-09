from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Event, EventToSubscriber
from django.urls import reverse_lazy

from django.http import HttpResponseRedirect, HttpResponse

from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin

from django.conf import settings
from django.core.mail import send_mail


# Список всех событий
class EventListView(ListView):
    model = Event
    template_name = "home.html"


# Конкретное событие
class EventDetail(DetailView):
    permission_classes = [IsAuthenticated]

    model = Event
    template_name = 'events/event_detail.html'

    def get_context_data(self, **kwargs):
        context = super(EventDetail, self).get_context_data(**kwargs)
        context['events_to_subscribers'] = EventToSubscriber.objects.all()
        context['current_user'] = self.request.user

        return context



# Создание нового события
class EventCreate(PermissionRequiredMixin, CreateView):
    permission_classes = [IsAuthenticated]
    permission_required = 'app.add_event'
    permission_denied_message = ""

    model = Event
    template_name = 'events/event_create.html'
    fields = ('EventName', 'EventDate',)
    success_url = reverse_lazy('home')

    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)


# Редактирование события
class EventUpdate(PermissionRequiredMixin, UpdateView):
    model = Event
    permission_classes = [IsAuthenticated]
    permission_required = 'app.change_event'
    permission_denied_message = ""

    template_name = 'events/event_update.html'
    context_object_name = 'event'
    fields = ('EventName', 'EventDate',)

    success_url = reverse_lazy('home')
    success_msg = 'Запись успешно обновлена'

    def get_context_data(self,**kwargs):
        kwargs['update'] = True
        return super().get_context_data(**kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.request.user != kwargs['instance'].owner:
            return self.handle_no_permission()
        return kwargs


# Удаление события
class EventDelete(LoginRequiredMixin, DeleteView):
    model = Event
    permission_classes = [IsAuthenticated]
    permission_required = 'app.delete_event'
    permission_denied_message = ""

    template_name = 'events/event_confirm_delete.html'
    success_url = reverse_lazy('home')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.request.user != self.object.owner:
            return self.handle_no_permission()
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)


# Функция подписки 
def EventSubscribe(request, event):
    current_user = request.user
    event_id = event
    current_event = Event.objects.get(pk=event_id)
    current_event_creator_email = current_event.owner.email

    output = "Спасибо за подписку!<br> <h3><a href='/event/{0}'>Обратно</a></h3>".format(event_id)

    new_subscriber = EventToSubscriber.objects.create()
    new_subscriber.event.add(event_id)
    new_subscriber.subscriber.add(current_user)

    send_mail('На ваше событие подписались', 'Поздравляем! На ваше событие подписался {0}!'.format(current_user), settings.EMAIL_HOST_USER, [current_event_creator_email])
    
    return HttpResponse(output)
