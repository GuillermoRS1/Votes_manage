from django.urls import path

from .views import SignUpView


urlpatterns = [
    # To create the url to the signUp form
    path("signup/", SignUpView.as_view(), name="signup"),
]