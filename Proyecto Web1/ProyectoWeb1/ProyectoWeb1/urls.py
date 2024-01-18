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


urlpatterns = [
    path('admin/', admin.site.urls),

    # URLS de los modelos creados
    path("", inicio, name="Inicio"),
    path("productos/", ver_productos, name="Productos"),
    path("perfumes/", ver_perfumes, name="Perfumes"),
    path("cremacorporal/", ver_cremacorporal, name="Crema Corporal"),

    # URLS para cear datos
    path("nuevoPerfume/", agregar_perfume),
    path("nuevaCremaCorporal/", agregar_cremacorporal),

    # URLS buscar productos
    path("buscarproductos/", buscar_productos),
    path("resultadosproductos/", resultado_buscar_productos),
    
]

