from django import forms
from django.contrib.auth.models import User


from bson import Binary, Code
from bson.json_util import dumps
from bson.json_util import loads
import json
import os


from django.template import RequestContext


class FormEntrada(forms.Form):
    file_clase = forms.FileField(label='Selecciona un archivo csv con nombres y dnis de la clase',required=False)




class SalaForm(forms.Form):
        nombre = forms.CharField(max_length=150, help_text="Introduce nombre sala")
        descripcion = forms.CharField(max_length=150, help_text="Introduce descripcion sala")
        
