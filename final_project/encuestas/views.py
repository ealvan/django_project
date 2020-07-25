from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
	return HttpResponse("Aqui estara nuestro home")
def detalle(request):
	return HttpResponse("Aqui estara la pregunta publicada")
def tablon(request):
	return HttpResponse("Aqui se mostraran la primeras cinco preguntas publicadas")
def editar(request):
	return HttpResponse("aqui se editara la pregunta")
