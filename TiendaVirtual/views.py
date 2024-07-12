from django.shortcuts import render
from .models import Prenda

def inicio(request):
    return render(request, "TiendaVirtual/inicio.html", {"esInicio": True})

def catalogo(request):
    prendas = Prenda.objects.all()
    return render(request, 'TiendaVirtual/catalogo.html', {'prendas': prendas})

def login(request):
    return render(request, "TiendaVirtual/login.html", {"esInicio": False})