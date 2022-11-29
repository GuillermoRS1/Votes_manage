from django.urls import path
from . import views

app_name = 'polls'
# We create the urls to be able to see the views created on the web page
urlpatterns = [
    # In the url ex: /polls/
    path('', views.IndexView.as_view(), name='index'),
    # In the url ex: /polls/5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # In the url ex: /polls/5/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # In the url ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]