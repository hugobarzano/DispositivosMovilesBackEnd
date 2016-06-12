from django.conf.urls import patterns, url
from . import views
from TalkToTheHandApp import views
from TalkToTheHandApp.views import *

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^nuevaSala$', views.salaCreator, name='salaCreator'),
    url(r'^salasJson/$', views.salasJson, name='salasJson'),
    url(r'^sala/(?P<id_sala>[\w\-]+)/$', views.sala, name='sala'),
    url(r'^enviar/$', views.enviar, name='enviar'),
    url(r'^updateSala/$', views.updateSala, name='updateSala'),

]
