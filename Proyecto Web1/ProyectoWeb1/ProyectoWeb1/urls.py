"""
URL configuration for ProyectoWeb1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from AppNatura.views import *
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),

    # URLS de los modelos creados
    path("", inicio, name="Inicio"),
    path("productos/", ver_productos, name="Productos"),
    path("perfumes/", ver_perfumes, name="Perfumes"),
    path("cremacorporal/", ver_cremacorporal, name="Crema Corporal"),

    # URLS para cear datos
    path("nuevoPerfume/", agregar_perfume, name= "Nuevo Perfume"),
    path("nuevaCremaCorporal/", agregar_cremacorporal, name="Nueva Crema"),

    # URLS buscar productos
    path("buscarproductos/", buscar_productos),
    path("resultadosproductos/", resultado_buscar_productos),

    # URLS actualizar
    path("actualizarperfume/<perfume_nombre>", actualizar_perfume, name="Actualizar Perfume"),
    
    # URLS buscar productos
    path("eliminarperfume/<perfume_nombre>", eliminar_perfume, name="Eliminar Perfume"),

    # URLS crud
    path("listacremacorporal/", ListaCremaCorporal.as_view(), name="Lista Crema Corporal"),
    path("crearcremacorporal/", CrearCremaCorporal.as_view(), name="Crear Crema Corporal"),
    path("actualizarcremacorporal/", ActualizarCremaCorporal.as_view(), name="Actualizar Crema Corporal"),
    path("borrarcremacorporal/", BorrarCremaCorporal.as_view(), name= "Borrar Crema Corporal"),

    #REGISTRO
    path("login/", inicio_sesion, name="Iniciar Sesion"),
    path("registro/", registro, name="Registrarse"),
    path("logout/", cerrar_sesion, name="Cerrar Sesion"),
]

