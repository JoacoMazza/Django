from django.shortcuts import render

# Create your views here.
from .models import *

def index(request):
    registro_clientes = Cliente.objects.all()
    contexto = {'clientes': registro_clientes}
    return render(request, 'index.html', contexto)