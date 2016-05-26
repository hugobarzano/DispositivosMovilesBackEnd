from django import forms
from django.contrib.auth.models import User
from ControlUsuarios.models import *


from bson import Binary, Code
from bson.json_util import dumps
from bson.json_util import loads
import json
import os
from ControlUsuarios.views import *


from django.template import RequestContext


class FormEntrada(forms.Form):
    file_clase = forms.FileField(label='Selecciona un archivo csv con nombres y dnis de la clase',required=False)




class SessionForm(forms.Form):
        session_tag = forms.CharField(max_length=150, help_text="Introduce La clave de assitencia")

############### REGISTRO DE USUARIOS #################
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('dni',)
