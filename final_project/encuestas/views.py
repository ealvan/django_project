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

def crear_opcion(request,preguntaID):
	try:
		pregunta = Pregunta.objects.get(id=preguntaID)
	except:
		raise Http404("no existe esta pregunta")
	if request.method == "POST":
		try:
			pregunta.opcion_set.create(opcion_txt=request.POST['opcion'],votos=0)
		except:
			raise Http404("lo sentimos no se pudo crear la bbdd")
		return HttpResponseRedirect(reverse('encuestas:detalle', args=(pregunta.id,)))
	else:
		return render(request,'encuestas/crear_opcion.html',{'pregunta':pregunta,})

def tablon(request):
	
	lista = Pregunta.objects.all()
	if lista:
		return render(request,'encuestas/tablon.html',{'lista':lista,})
	else:
		raise Http404("lo sentimos, aun no se han publicado preguntas")

	return HttpResponse("Aqui se mostraran la primeras cinco preguntas publicadas")
