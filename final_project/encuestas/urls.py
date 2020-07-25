from django.urls import path
from encuestas import views	

app_name = 'encuestas'

urlpatterns = [
	path('', views.home, name='home'),
	path('detalle/',views.detalle, name="detalle"),
	path('tablon/',views.tablon, name = 'tablon'),
	path('editar/', views.editar, name = 'editar'),
	
]