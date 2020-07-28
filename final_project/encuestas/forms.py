from django import forms

from .models import Pregunta
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PreguntaForm(forms.ModelForm):
  class Meta:
    model = Pregunta
    fields = [
        'pregunta_txt',
        ]
class CrearUsuarioForm(UserCreationForm):
	class Meta:
		model = User
		fields = [
		'username',
		'email',
		'password1',
		'password2',
		]