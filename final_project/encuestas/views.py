from django.shortcuts import render
from django.http import HttpResponse,Http404,HttpResponseRedirect
from encuestas.models import Pregunta,Opcion
from django.urls import reverse
# Create your views here.

def home(request):
	return HttpResponse("Aqui estara nuestro home")
def detalle(request,preguntaID):
	try:
		pregunta = Pregunta.objects.get(pk=preguntaID)
	except:
		raise Http404("la pregunta no existe")
	return render(request,'encuestas/detalle.html',{'pregunta':pregunta})
def votar(request,preguntaID):
	try:
		pregunta = Pregunta.objects.get(pk=preguntaID)
	except:
		raise Http404("la pregunta no existe")
	try:
		opcion_selec = pregunta.opcion_set.get(pk=request.POST['opcion'])
	except:
		diccionario = {'pregunta':pregunta, 'error':'tu no seleccionaste una opcion'}
		return render(request,'encuestas/detalle.html',diccionario)
	else:
		opcion_selec.votos += 1
		opcion_selec.save()
		return HttpResponseRedirect(reverse('encuestas:resultado',args=(pregunta.id,)))

def resultado(request,preguntaID):
	try:
		pregunta = Pregunta.objects.get(pk = preguntaID)
	except:
		raise Http404("la pregunta no existe")
	return render(request,'encuestas/resultado.html',{'pregunta':pregunta})


def tablon(request):
	return HttpResponse("Aqui se mostraran la primeras cinco preguntas publicadas")
def editar(request):
	return HttpResponse("aqui se editara la pregunta")
