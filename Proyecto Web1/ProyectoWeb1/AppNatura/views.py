from django.shortcuts import render
from django.http import HttpResponse
from AppNatura.models import *
from AppNatura.forms import *
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def inicio(request):
    return render(request,"AppNatura/inicio.html")

def ver_productos(request):
    
    return render(request,"AppNatura/productos.html")





#AGREGAR perfume
@login_required
def ver_perfumes(request):

    mis_perfumes = Perfume.objects.all()
    info = {"perfumes":mis_perfumes}

    return render(request,"AppNatura/perfumes.html", info)

@login_required
def agregar_perfume(request):

    if request.method == "POST":
        info_formulario = Perfumeformulario(request.POST)
        
        if info_formulario.is_valid():
            info = info_formulario.cleaned_data
            nuevo_perfume = Perfume(nombre=info["nombre"], contenido_neto=info["contenido neto"], vto=info["vto"], precio=info["precio"],)
            nuevo_perfume.save()
            return render(request, "AppNatura/inicio.html")
    
    else:
         info_formulario = Perfumeformulario()

    
    return render(request, "AppNatura/formularioperfume.html", {"formulario":info_formulario})
    
    




def actualizar_perfume(request, perfume_nombre):
    
    perfume_elegido = Perfume.objects.get(nombre=perfume_nombre)
    
    if request.method == "POST":
        info_formulario = Perfumeformulario(request.POST)

        if info_formulario.is_valid():
            
            info = info_formulario.cleaned_data
            
            perfume_elegido.nombre = info["nombre"]
            perfume_elegido.contenido_neto = info["contenido_neto"]
            perfume_elegido.vto = info["vencimiento"]
            perfume_elegido.precio = info["precio"]
            
            perfume_elegido.save()

            return render(request, "AppNatura/inicio.html")
    else:
        info_formulario = Perfumeformulario(initial={"nombre":perfume_elegido.nombre,
                                                     "contenido neto":perfume_elegido.contenido_neto,
                                                     "vencimiento":perfume_elegido.vto, 
                                                     "precio":perfume_elegido.precio })

    return render(request, "AppNatura/actualizar_perfume.html", {"formulario":info_formulario})


def eliminar_perfume(request, perfume_nombre):

    perfume_elegido = Perfume.objects.get(nombre=perfume_nombre)

    perfume_elegido.delete()
    return render(request, "AppNatura/perfumes.html")
    








#CREMA CORPORAL


def ver_cremacorporal(request):

    return render(request,"AppNatura/cremacorporal.html")

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

    return render(request, "AppNatura/formulariocorporal.html", {"formulario":info_formulario})


def resultado_buscar_productos(request):
    if  request.method=="GET":

        nombre_pedido = request.GET["nombre"]
        resultados_perfumes = Perfume.objects.filter(nombre__icontains=nombre_pedido)

        return render(request, "AppNatura/buscarproductos.html", {"nombre":resultados_perfumes})

    else:
        return render(request, "AppNatura/buscarproductos.html")



def buscar_productos(request):

    return render(request, "AppNatura/buscarproductos.html")




class ListaCremaCorporal(ListView):
    model = CremaCorporal
    template_name = "AppNatura/cremacorporal_list.html"

class CrearCremaCorporal(CreateView):

    model = CremaCorporal
    template_name = "AppNatura/crear_cremacorporal.html"
    fields = ["nombre", "contenido_neto", "vto", "precio"]
    success_url = "/listacremacorporal/"

class ActualizarCremaCorporal(UpdateView):

    model = CremaCorporal
    template_name = "AppNatura/crear_cremacorporal.html"
    fields = ["nombre", "contenido_neto", "vto", "precio"]
    success_url = "/listacremacorporal/"

class BorrarCremaCorporal(DeleteView):

    model = CremaCorporal
    template_name = "AppNatura/borrar_cremacorporal.html"
    success_url = "/listacremacorporal/"


# vistas de register/login/logout
    
def inicio_sesion(request):
    if request.method == "POST":
        formulario = AuthenticationForm(request, data = request.POST)
        
        if formulario.is_valid():

            info = formulario.cleaned_data
            usuario = info["username"]
            contra = info["password"]

            usuario_actual = authenticate(username=usuario, password=contra)

            if usuario_actual is not None:
                login(request, usuario_actual)
                
                return render(request,"AppNatura/inicio.html", {"mensaje":f"Bienvenido {usuario}"} )
            else:
                return render(request, "AppNatura/inicio.html", {"mensaje": "Error, datos incorrectos"} )
    
    else: 
            formulario = AuthenticationForm()

    return render(request, "registro/inicio_sesion.html", {"formu":formulario})



def registro(request):

    if request.method == "POST":
        formulario = RegistrarUsuario(request.POST)
        
        if formulario.is_valid():
            
            info = formulario.cleaned_data
            usuario = info["username"]
            formulario.save()
            
            return render(request, "AppNatura/inicio.html", {"mensaje":f"Bienvenido {usuario}"} )

    else:
        formulario = RegistrarUsuario()
    
    return render(request, "registro/registrar_usuario.html", {"formu":formulario})

def editar_perfil(request):
    usuario_actual = request.user
    
    if request.method == "POST":
        formulario = RegistrarUsuario(request.POST)
        
        if formulario.is_valid():
            
            info = formulario.cleaned_data
            usuario_actual.first_name = info["first_name"]
            usuario_actual.last_name = info["last_name"]
            usuario_actual.email = info["email"]
            usuario_actual.save()
            
            return render(request, "AppNatura/inicio.html" )

    else:
        formulario = RegistrarUsuario((initial={"frist_name":usuario_actual.frist_name,
                                                     "last_name":perfume_elegido.contenido_neto,
                                                     "vencimiento":perfume_elegido.vto, 
                                                     "precio":perfume_elegido.precio, }
                                    ))
    
    return render(request, "registro/registrar_usuario.html", {"formu":formulario})

def cerrar_sesion(request):
    logout(request)

    return render(request, "registro/cerrar_sesion.html")
