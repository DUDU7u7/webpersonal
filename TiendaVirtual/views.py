from django.shortcuts import render

def inicio(request):
    return render(request, "TiendaVirtual/inicio.html", {"esInicio": True})

def registro(request):
    return render(request, "TiendaVirtual/registro.html", {"esInicio": False})

def login(request):
    return render(request, "TiendaVirtual/login.html", {"esInicio": False})