from django.shortcuts import render
from django.http import HttpResponse
from AppNatura.models import *
from AppNatura.forms import *
# Create your views here.

def inicio(request):
    return render(request,"AppNatura/inicio.html")

def ver_productos(request):
    
    return render(request,"AppNatura/productos.html")


def ver_perfumes(request):

    return render(request,"AppNatura/perfumes.html")

def ver_cremacorporal(request):

    return render(request,"AppNatura/cremacorporal.html")

#AGREGAR perfume

def agregar_perfume(request):

    if request.method == "POST":
        info_formulario = Perfumeformulario(request.POST)

        if info_formulario.is_valid():
            info = info_formulario.cleaned_data
            nuevo_perfume = Perfume(nombre=info["nombre"], contenido_neto=info["neto"], vto=info["vto"], precio=info["precio"],)
            nuevo_perfume.save()
            return render(request, "AppNatura/inicio.html")
    
    else:
        info_formulario = Perfumeformulario()

    return render(request, "AppNatura/formularioperfume.html", {"formulario":info_formulario})


def agregar_cremacorporal(request):

    if request.method == "POST":
        info_formulario = Corporalformulario(request.POST)

        if info_formulario.is_valid():
            info = info_formulario.cleaned_data
            nuevo_corporal = CremaCorporal(nombre=info["nombre"], contenido_neto=info["neto"], vto=info["vto"], precio=info["precio"],)
            nuevo_corporal.save()
            return render(request, "AppNatura/inicio.html")
    
    else:
        info_formulario = Corporalformulario()

    return render(request, "AppNatura/formulariocorporal.html")


def resultado_buscar_productos(request):
    if  request.method=="GET":

        nombre_pedido = request.GET["nombre"]
        resultados_perfumes = Perfume.objects.filter(nombre__icontains=nombre_pedido)

        return render(request, "AppNatura/buscarproductos.html", {"nombre":resultados_perfumes})

    else:
        return render(request, "AppNatura/buscarproductos.html")



def buscar_productos(request):

    return render(request, "AppNatura/buscarproductos.html")




"""def agregar_perfume(request):
     if request.method=="POST":
         
        perfume1 = Perfume(
                        nombre=request.POST["nombre"], 
                        contenido_neto=request.POST["contenido neto"], 
                        vto=request.POST["vto"], 
                        precio=request.POST["precio"]
                        )
        perfume1.save()

     return render(request,"AppNatura/nuevoperfume.html")

"""