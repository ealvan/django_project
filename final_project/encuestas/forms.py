from django import forms

from .models import Pregunta

class FotoForm(forms.ModelForm):
  class Meta:
    model = Pregunta
    fields = [
        'pregunta_txt',
        'pub_fecha',
        ]
