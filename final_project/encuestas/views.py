from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,Http404,HttpResponseRedirect
from encuestas.models import Pregunta,Opcion
from django.urls import reverse
from .forms import PreguntaForm
from django.contrib.auth.forms import UserCreationForm
from encuestas.forms import CrearUsuarioForm
# Create your views here.

def home(request):
	return HttpResponse("Aqui estara nuestro home")
def registro(request):
	form = CrearUsuarioForm()
	if request.method == 'POST':
		form = CrearUsuarioForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('encuestas:home',))
	contexto = {'form':form}
	return render(request,'registro.html',contexto)
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
        pregunta = Pregunta.objects.get(id = preguntaID)
    except:
        raise Http404("no existe esta pregunta")

    if request.method == "POST":
        cadena = request.POST.get("lista");
        lista = cadena.split(",")
        try:
            for x in range(len(lista) - 1):
                pregunta.opcion_set.create(opcion_txt = lista[x], votos = 0)
                #pregunta.opcion_set.create(opcion_txt = request.POST['opcion'],votos = 0)
        except:
            raise Http404("lo sentimos no se pudo crear la bbdd")
        return HttpResponseRedirect(reverse('encuestas:detalle', args = (pregunta.id,)))
    else:
        return render(request,'encuestas/crear_opcion.html',{'pregunta':pregunta,})

def tablon(request):
	
	lista = Pregunta.objects.all()
	if lista:
		return render(request,'encuestas/tablon.html',{'lista':lista,})
	else:
		raise Http404("lo sentimos, aun no se han publicado preguntas")

	return HttpResponse("Aqui se mostraran la primeras cinco preguntas publicadas")

def preguntaCreateView(request):
        form = PreguntaForm(request.POST or None)
        if form.is_valid():
            form.save()
            form = PreguntaForm()

        context = {
                'form': form
                }
        return render(request, 'encuestas/crearPregunta.html', context)
