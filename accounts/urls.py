from django.urls import path
from .views import SignupView, userProfileView

urlpatterns = [
    path("signup/", SignupView.as_view(), name='signup'),
    path("profile/", userProfileView, name='profile'),
]
