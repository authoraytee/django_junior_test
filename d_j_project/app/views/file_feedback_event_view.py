from django.db.models.base import Model
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin

from ..models import FileFeedbackEvent, FileFeedbackEventToSubscriber
from ..serializers import EventsSerializer
from urllib import request

from django.conf import settings
from django.core.mail import send_mail

class FilefeedbackEventViewSet(ModelViewSet):
    queryset = FileFeedbackEvent.objects.all()
    serializer_class = EventsSerializer
    permission_classes = [IsAuthenticated]


class FilefeedbackEventListView(ListView):
    model = FileFeedbackEvent
    template_name = "home.html"


class FilefeedbackEventDetail(DetailView):
    permission_classes = [IsAuthenticated]

    model = FileFeedbackEvent
    template_name = 'event_detail.html'

    def get_context_data(self, **kwargs):
        context = super(EventDetail, self).get_context_data(**kwargs)
        context['events_to_subscribers'] = FileFeedbackEventToSubscriber.objects.all()
        context['current_user'] = self.request.user
        return context



def FilefeedbackEventSubscribe(request, event):
    current_user = request.user
    # event_id уже определен 
    event_id = event
    current_event = FileFeedbackEvent.objects.get(pk=event_id)
    current_event_creator_email = current_event.owner.email

    output = "Спасибо за подписку!<br> <h3><a href='/event/{0}'>Обратно</a></h3>".format(event_id)

    new_subscriber = FileFeedbackEventToSubscriber.objects.create()
    new_subscriber.event.add(event_id)
    new_subscriber.subscriber.add(current_user)

    send_mail('На ваше событие подписались', 'Поздравляем! На ваше событие подписался {0}!'.format(current_user), settings.EMAIL_HOST_USER, [current_event_creator_email])
    
    return HttpResponse(output)








class FilefeedbackEventCreate(PermissionRequiredMixin, CreateView):
    permission_classes = [IsAuthenticated]
    permission_required = 'app.add_event'
    permission_denied_message = ""

    model = FileFeedbackEvent
    template_name = 'event_create.html'
    fields = ('EventName', 'EventDate',)
    success_url = reverse_lazy('home')

    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)


class FilefeedbackEventUpdate(PermissionRequiredMixin, UpdateView):
    model = FileFeedbackEvent
    permission_classes = [IsAuthenticated]
    permission_required = 'app.change_event'
    permission_denied_message = ""

    template_name = 'event_update.html'
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


class FilefeedbackEventDelete(LoginRequiredMixin, DeleteView):
    model = FileFeedbackEvent
    permission_classes = [IsAuthenticated]
    permission_required = 'app.delete_event'
    permission_denied_message = ""

    template_name = 'event_confirm_delete.html'
    success_url = reverse_lazy('home')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.request.user != self.object.owner:
            return self.handle_no_permission()
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)



