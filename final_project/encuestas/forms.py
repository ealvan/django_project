from django import forms

from .models import Pregunta

class PreguntaForm(forms.ModelForm):
  class Meta:
    model = Pregunta
    fields = [
        'pregunta_txt',
        ]
