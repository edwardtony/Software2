from django.conf.urls import url, include
from apiREST import views

from django.conf.urls import url
urlpatterns = [
    url(r'^data/', views.data),
]
