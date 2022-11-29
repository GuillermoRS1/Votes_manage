from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import TemplateView

urlpatterns = [
    # To point the root URLconf at the polls.urls module
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    #  We add the auth app to our project-level in order to use it in our project
    path("accounts/", include("django.contrib.auth.urls")),
    # We create the url for the page to create an account
    path("accounts/", include("accounts.urls")),
    # We create the url to redirect to the home page
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
]
