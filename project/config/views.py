from django.http import HttpResponse
from django.template import Context, Template
from datetime import datetime
from django.shortcuts import render


def saludo(request):
	return HttpResponse("Hola Django - Coder")

def saludo_vista(request):
	return HttpResponse("<h1>Segunda vista</h1>")

def nombre(request, nombre: str, apellido: str):
	nombre =  nombre.capitalize()
	apellido = apellido.capitalize()
	return HttpResponse(f"{apellido}, {nombre}")

def probando_template(request):
	mi_html = open("./templates/template1.html")
	mi_template = Template(mi_html.read())
	mi_html.close()
	nombre = "Juan"
	apellido = "Perez"
	datos = {"nombre": nombre, "apellido": apellido}
	mi_contexto = Context(datos)
	mi_documento = mi_template.render(mi_contexto)
	return HttpResponse(mi_documento)

def fechaHora(request):
	ahora = datetime.now().strftime(r"%Y-%m-%d %H:%M")
	return HttpResponse(ahora)

