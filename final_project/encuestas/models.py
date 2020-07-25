from django.db import models
from django.utils import timezone
import datetime
# Create your models here.
class Pregunta(models.Model):
	pregunta_txt = models.CharField(max_length=100)
	pub_fecha  = models.DateTimeField('Fecha de Publicacion')
	def __str__(self):
		return f'{self.pregunta_txt}'

class Opcion(models.Model):
	pregunta_txt = models.ForeignKey(Pregunta, on_delete = models.CASCADE)
	opcion_txt = models.CharField(max_length=100)
	votos = models.IntegerField(default=0)	
	def __str__(self):
		return f'opinion: {self.opcion_txt} votos: {self.votos}'