from django.conf.urls import patterns, url
from django.views.decorators.csrf import csrf_exempt
from ControlUsuarios import views
from ControlUsuarios.views import *


urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^sesion/$', views.sesion, name='sesion'),
        url(r'^alumnosJson/$', views.alumnosJson, name='alumnosJson'),
        url(r'^CheckFromQr/$', views.CheckFromQr, name='CheckFromQr'),
        url(r'^CheckFromNfc/$', views.CheckFromNfc, name='CheckFromNfc'),
        (r'^Preferencias/$',Preferencias.as_view()),
        url(r'^register/$', views.register, name='register'),
        url(r'^login/$', views.user_login, name='login'),
        url(r'^logout/$', views.user_logout, name='logout'),
        url(r'^androidLogin/$', views.androidLogin, name='androidLogin'),
        url(r'^androidRegister/$', views.androidRegister, name='androidRegister'),
        )
