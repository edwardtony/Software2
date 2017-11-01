from django.conf.urls import url, include
from apiREST import views

from django.conf.urls import url
urlpatterns = [
    url(r'^scenarios/', views.scenarios),
    url(r'^characters/', views.characters),
    url(r'^player_list/', views.player_list),
]
