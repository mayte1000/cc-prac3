from django.http import JsonResponse, HttpResponse
from .models import Productos
from django.shortcuts import render
import json

# Create your views here.
def productosAll(request):
    productos = list(Productos.objects.values())
    return JsonResponse(productos, safe=False)

def index(request):
    return render(request,'index.html')

def alimentos(request):
    return render(request,'alimentos.html')

def acercade(request):
    return render(request,'acercade.html')

def contacto(request):
    return render(request,'contacto.html')

def accesorios(request):
    return render(request,'accesorios.html')

def cuidadosmascotas(request):
    return render(request,'cuidadosmascotas.html')

def carrito(request):
    productos = json.dumps(list(Productos.objects.values()))
    return render(request,'carrito.html', {
        'productos':productos
    })

def descripcionRoyalcanin(request):
    return render(request,'descripcion-imagen-royalcanin.html')

def descripcionRoyalRegular(request):
    return render(request,'descripcion-imagen-royalregularfit.html')

def descripcionPurinaProplan(request):
    return render(request,'descripcion-imagen-purinaproplan.html')

def descripcionBalanced(request):
    return render(request,'descripcion-imagen-balanced.html')

def descripcionEukanuba(request):
    return render(request,'descripcion-imagen-eukanuba.html')

def descripcionExcellent(request):
    return render(request,'descripcion-imagen-excellent.html')

def descripcionOldprince(request):
    return render(request,'descripcion-imagen-oldprince.html')

def descripcionInfinity(request):
    return render(request,'descripcion-imagen-infinity.html')

def login(request):
    return render(request,'login.html')

def registro(request):
    return render(request,'registro.html')

def recuperarContrasenia(request):
    return render(request,'recuperar-contrasenia.html')