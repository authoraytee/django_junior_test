from django.contrib import admin
from django.urls import path, include
 

from django.conf.urls import url


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('feedbackfile_app/', include('feedbackfile_app.urls')),
    path('', include('app.urls')),
]
