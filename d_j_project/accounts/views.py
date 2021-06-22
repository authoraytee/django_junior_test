from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import ListView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import PermissionRequiredMixin

from app.models import Event, EventToSubscriber

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class UserProfile(PermissionRequiredMixin, ListView):
    context_object_name = 'home_list'
    permission_required = 'app.view_event'    
    model = User
    template_name = "user_profile.html"

    def get_context_data(self, **kwargs):
        context = super(UserProfile, self).get_context_data(**kwargs)
        context['events_to_subscribers'] = EventToSubscriber.objects.all()
        return context



