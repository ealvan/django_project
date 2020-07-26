from django.urls import path
from encuestas import views	

app_name = 'encuestas'

urlpatterns = [
	path('', views.home, name='home'),
	path('<int:preguntaID>/',views.detalle, name="detalle"),
	path('tablon/',views.tablon, name = 'tablon'),
	path('editar/', views.editar, name = 'editar'),
	path('<int:preguntaID>/votar/',views.votar,name = 'votar'),
	path('<int:preguntaID>/resultado/',views.resultado,name='resultado'),
	path('<int:preguntaID>/crear_opcion/',views.crear_opcion, name='crear_opcion'),
	path('tablon/',views.tablon, name='tablon'),
]