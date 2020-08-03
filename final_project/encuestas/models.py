from django.db import models
from django.utils import timezone
# Create your models here.
class Pregunta(models.Model):
    pregunta_txt = models.CharField(max_length=100)
    comida='cm'
    deporte='dp'
    salud='sa'
    farandula='fa'
    noticias='no'
    cine='cn'
    ciencias='ci'
    opciones = [('comida','Comida'),
    			('deporte','Deporte'),
    			('salud','Salud'),
    			('farandula','Farandula'),
    			('noticias','Noticias'),
    			('cine','Cine'),
    			('ciencias','Ciencias'),
            	]
    area = models.CharField(max_length=20,choices=opciones,default='salud',)
    pub_fecha = models.DateTimeField('Fecha de Publicacion', default = timezone.now())
    def __str__(self):
        return f'{self.pregunta_txt}'

class Opcion(models.Model):
	pregunta_txt = models.ForeignKey(Pregunta, on_delete = models.CASCADE)
	opcion_txt = models.CharField(max_length=100)
	votos = models.IntegerField(default=0)	
	def __str__(self):
		return f'opinion: {self.opcion_txt} votos: {self.votos}'

