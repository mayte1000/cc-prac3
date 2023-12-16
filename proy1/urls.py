"""
URL configuration for proy1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from app1 import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('alimentos/', views.alimentos),
    path('acercade/', views.acercade),
    path('contacto/', views.contacto),
    path('accesorios/', views.accesorios),
    path('cuidadosmascotas/', views.cuidadosmascotas),
    path('carrito/', views.carrito),
    path('productos/', views.productosAll),    
    path('descripcionRoyalcanin/', views.descripcionRoyalcanin),
    path('descripcionRoyalRegular/', views.descripcionRoyalRegular),
    path('descripcionPurinaProplan/', views.descripcionPurinaProplan),
    path('descripcionBalanced/', views.descripcionBalanced),
    path('descripcionEukanuba/', views.descripcionEukanuba),
    path('descripcionExcellent/', views.descripcionExcellent),
    path('descripcionOldprince/', views.descripcionOldprince),
    path('descripcionInfinity/', views.descripcionInfinity),
    path('login/', views.login),
    path('registro/', views.registro),
    path('recuperarContrasenia/', views.recuperarContrasenia),

]
