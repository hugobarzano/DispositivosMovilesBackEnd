from django.conf.urls import patterns, url
from . import views
from TalkToTheHandApp import views
from TalkToTheHandApp.views import *

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^nuevaSala$', views.salaCreator, name='salaCreator'),
    url(r'^salasJson/$', views.salasJson, name='salasJson'),

]
