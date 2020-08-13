from django import forms

from .models import Pregunta
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PreguntaForm(forms.ModelForm):
  class Meta:
    model=Pregunta 
    fields = ['pregunta_txt','area']
    widgets = {
            'pregunta_txt':forms.TextInput(attrs={'class':'pregunta',
                                            'placeholder':'ingrese su pregunta'}),
        }
  def clean_pregunta_txt(self):
    ''' hara una validacion, si no hay un '?' o '¿' en la pregunta'''
    pregunta = self.cleaned_data.get("pregunta_txt")
    fin = pregunta[-1]
    ini = pregunta[0]
    if fin != '?' or ini != '¿':
       raise forms.ValidationError("una pregunta debe tener un '¿' y '?'")
    return pregunta
    
class CrearUsuarioForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
        'username',
        'email',
        'password1',
        'password2',
        ]
        widgets = {
            'username':forms.TextInput(attrs={'class':'pregunta',
                                            'placeholder':'ingrese su usuario'}),
            'email':forms.EmailInput(attrs={'class':'special',
                                            'placeholder':'ingrese su email'}),
        }
