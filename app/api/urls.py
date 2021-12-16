from django.conf.urls import url
from api import views

urlpatterns = [
    url('process-songs/', views.ProcessSongsList.as_view()),
]
