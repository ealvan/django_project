from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
<<<<<<< HEAD

def encuestaCreateView(request):
    form = encuestaForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = FotoForm()

    context = {
            'form': form
            }
    return render(request, 'encuestas/encuestaCreate.html', context)

=======
def home(request):
	return HttpResponse("Aqui estara nuestro home")
def detalle(request):
	return HttpResponse("Aqui estara la pregunta publicada")
def tablon(request):
	return HttpResponse("Aqui se mostraran la primeras cinco preguntas publicadas")
def editar(request):
	return HttpResponse("aqui se editara la pregunta")
>>>>>>> origin/experimental
