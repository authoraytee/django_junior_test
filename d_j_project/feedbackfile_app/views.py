from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import FileFeedbackEvent, FileFeedbackEventToSubscriber
from .serializers import EventsSerializer
from .models import FileFeedbackEventToSubscriber
from .forms import FileFieldForm, FeedbackForm
from django.urls import reverse_lazy

from django.http import HttpResponseRedirect, HttpResponse

from rest_framework.viewsets import ModelViewSet

from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin

from django.conf import settings
from django.core.mail import send_mail



class FileFeedbackEventListView(ListView):
    model = FileFeedbackEvent
    template_name = "feedback/filefeedback_events_home.html"


class FileFeedbackEventDetail(DetailView):
    permission_classes = [IsAuthenticated]

    model = FileFeedbackEvent
    template_name = 'feedback/filefeedback_event_detail.html'

    def get_context_data(self, **kwargs):
        context = super(FileFeedbackEventDetail, self).get_context_data(**kwargs)
        context['events_to_subscribers'] = FileFeedbackEventToSubscriber.objects.all()
        context['current_user'] = self.request.user
        return context


class FileFeedbackEventCreate(PermissionRequiredMixin, CreateView):
    permission_classes = [IsAuthenticated]
    permission_required = 'app.add_event'
    permission_denied_message = ""

    model = FileFeedbackEvent
    template_name = 'feedback/filefeedbackevent_create.html'
    fields = ('EventName', 'EventDate',)
    success_url = reverse_lazy('filefeedback_events_home')

    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)


class FileFeedbackEventUpdate(PermissionRequiredMixin, UpdateView):
    model = FileFeedbackEvent
    permission_classes = [IsAuthenticated]
    permission_required = 'app.change_event'
    permission_denied_message = ""

    template_name = 'feedback/filefeedback_event_update.html'
    context_object_name = 'event'
    fields = ('EventName', 'EventDate',)

    success_url = reverse_lazy('filefeedback_events_home')
    success_msg = 'Запись успешно обновлена'

    def get_context_data(self,**kwargs):
        kwargs['update'] = True
        return super().get_context_data(**kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.request.user != kwargs['instance'].owner:
            return self.handle_no_permission()
        return kwargs


class FileFeedbackEventDelete(LoginRequiredMixin, DeleteView):
    model = FileFeedbackEvent
    permission_classes = [IsAuthenticated]
    permission_required = 'app.delete_event'
    permission_denied_message = ""

    template_name = 'feedback/filefeedback_event_confirm_delete.html'
    success_url = reverse_lazy('filefeedback_events_home')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.request.user != self.object.owner:
            return self.handle_no_permission()
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)


#Отправкеа файла
class SendFileFeedback(CreateView): # новый
    model = FileFeedbackEventToSubscriber
    form_class = FileFieldForm
    template_name = 'feedback/send_feedback_file.html'
    success_url = reverse_lazy('feedback/filefeedback_events_home')

# Отправка фидбека
class SendFeedback(CreateView):
    model = FileFeedbackEventToSubscriber
    form_class = FeedbackForm
    template_name = 'feedback/send_feedback.html'
    success_url = reverse_lazy('feedback/filefeedback_events_home')

# Подписка
def EventSubscribe(request, event):
    current_user = request.user
    event_id = event
    current_event = FileFeedbackEvent.objects.get(pk=event_id)
    current_event_creator_email = current_event.owner.email

    new_subscriber = FileFeedbackEventToSubscriber.objects.create()
    new_subscriber.event.add(event_id)
    new_subscriber.subscriber.add(current_user)

    send_mail('На ваше событие подписались', 'Поздравляем! На ваше событие подписался {0}!'.format(current_user), settings.EMAIL_HOST_USER, [current_event_creator_email])
    
    output = "Спасибо за подписку!<br> <h3><a href='/feedbackfile_app/filefeedback_event/{0}'>Обратно</a></h3>".format(event_id)
    
    return HttpResponse(output)

