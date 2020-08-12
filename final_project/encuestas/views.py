from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect, JsonResponse
from encuestas.models import Pregunta,Opcion
from django.urls import reverse
from encuestas.forms import PreguntaForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login,logout,authenticate
from encuestas.forms import CrearUsuarioForm
from django.contrib.auth.decorators import login_required

from django.views import View


# Create your views here.

def home(request):
	return render(request,'encuestas/home.html',{})
def welcome(request):
	return render(request,'base2.html',{})
def registro(request):
	if request.user.is_authenticated:
		return HttpResponseRedirect(reverse('encuestas:home'))
	form = CrearUsuarioForm()
	if request.method == 'POST':
		form = CrearUsuarioForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('encuestas:home',))
	contexto = {'form':form}
	return render(request,'registro.html',contexto)

def login(request):
	if request.user.is_authenticated:
		mensaje='usted ya ha iniciado sesion'
		return render(request,'encuestas/home.html',{'mensaje':mensaje})
	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username,password=password)
		if user is not None:
			auth_login(request,user)
			return HttpResponseRedirect(reverse('encuestas:home',))
		else:
			mensaje = 'la contraseña o el nombre de usuario son incorrectos'
			return render(request,'login.html',{'mensaje':mensaje})
	return render(request,'login.html',{})

@login_required(login_url='login')
def logoutU(request):
	logout(request)
	return HttpResponseRedirect(reverse('login'))

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

@login_required(login_url='login')
def crear_opcion(request,preguntaID):
	try:
		pregunta = Pregunta.objects.get(id = preguntaID)
	except:
		raise Http404("no existe esta pregunta")

	if request.method == "POST":
		cadena = request.POST.get("lista");
		#print(cadena)
		lista = cadena.split(",")
		#print(lista)
		try:
			for x in range(len(lista) - 1):
				pregunta.opcion_set.create(opcion_txt = lista[x], votos = 0)
				#pregunta.opcion_set.create(opcion_txt = request.POST['opcion'],votos = 0)
		except:
			raise Http404("lo sentimos no se pudo crear la bbdd")
		return HttpResponseRedirect(reverse('encuestas:detalle', args = (pregunta.id,)))
	else:
		return render(request,'encuestas/crear_opcion.html',{'pregunta':pregunta,})
@login_required(login_url='login')
def tablon(request):
	lista = Pregunta.objects.all()
	if lista:
		return render(request,'encuestas/tablon.html',{'lista':lista,})
	else:
		raise Http404("lo sentimos, aun no se han publicado preguntas")

	return HttpResponse("Aqui se mostraran la primeras cinco preguntas publicadas")

@login_required(login_url='login')
def preguntaCreateView(request):

	if request.method == "POST":
		form = PreguntaForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("encuestas:tablon")
	else:
		form = PreguntaForm()
	context = {
	   'form': form,
	}
	return render(request, 'encuestas/crearPregunta.html', context)

@login_required(login_url='login')
def borrar(request,preguntaID):
	try:
		pregunta = Pregunta.objects.get(pk=preguntaID)
	except:
		raise Http404("lo sentimos, la pregunta no existe")
	try:
		pregunta.delete()
	except:
		raise Http404("lo sentimos ocurrio un inesperado error,intentelo mas tarde")
	return render(request,'encuestas/borrar.html',{})

class PreguntaQueryView(View):
	def get(self, request):
		queryset = Pregunta.objects.all()
		return JsonResponse(list(queryset.values()), safe = False)

def tablonAjaxView(request):
	return render(request, 'encuestas/tablonAjax.html', {})
