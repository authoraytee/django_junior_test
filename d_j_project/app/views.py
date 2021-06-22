from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin

from .models import Event
from .serializers import EventsSerializer


# class UserAccessMixin(PermissionRequiredMixin):
#     def dispatch(self, request, *args, **kwargs):
#         if (not self.request.user.is_authenticated):
#             return redirect_to_login(self.request.get_full_path(),
#             self.get_login_url(), self.get_redirect_field_name())
#         if (not self.has_permission()):
#             return redirect("/")
#         return super(UserAccessMixin, self).dispatch(request, *args, **kwargs)

# class PostUserWritePermission(BasePermission):
#     def has_object_permission(self, request, view, obj):
#         if request.method in SAFE_METHODS:
#             return True
#         return obj.owner == request.user





# from django.shortcuts import render
 
# def index(request):
#     queryset = Event.objects.all()
#     return render(request, "home.html", queryset)






class EventViewSet(ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventsSerializer
    permission_classes = [IsAuthenticated]

    #template_name = 'home.html'

    # def perform_create(self, serializer):
    #     serializer.validated_data["owner"] = self.request.user
    #     serializer.save()


class EventDetail(DetailView):
    permission_classes = [IsAuthenticated]

    model = Event
    template_name = 'event_detail.html'


class EventCreate(PermissionRequiredMixin, CreateView):
    permission_classes = [IsAuthenticated]
    permission_required = 'app.create_event'
    permission_denied_message = ""

    model = Event
    template_name = 'event_create.html'
    fields = ('EventName', 'EventDate',)
    success_url = reverse_lazy('home')

    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)


class EventUpdate(PermissionRequiredMixin, UpdateView):
    model = Event
    permission_classes = [IsAuthenticated]
    permission_required = 'app.change_event'
    permission_denied_message = ""

    template_name = 'event_update.html'
    context_object_name = 'event'
    fields = ('EventName', 'PublicationDate', 'EventDate',)

    success_url = reverse_lazy('edit_page')
    success_msg = 'Запись успешно обновлена'

    def get_context_data(self,**kwargs):
        kwargs['update'] = True
        return super().get_context_data(**kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.request.user != kwargs['instance'].owner:
            return self.handle_no_permission()
        return kwargs


class EventDelete(LoginRequiredMixin, DeleteView):
    model = Event
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

