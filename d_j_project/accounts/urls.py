from django.urls import path
 
from .views import SignUpView, UserProfile
 
urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('user/', UserProfile.as_view(), name="user_profile",)
]