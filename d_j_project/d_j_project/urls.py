from django.contrib import admin
from django.urls import path, include
 
from rest_framework.routers import SimpleRouter
from app.views import EventViewSet

from django.conf.urls import url

router = SimpleRouter()

router.register(r'events', EventViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('', include('app.urls')),
]

urlpatterns += router.urls