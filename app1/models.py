from django.db import models

# Create your models here.
class Productos(models.Model):
    nombre = models.CharField(max_length=200)
    precio = models.IntegerField(default=0)

class Clientes(models.Model):
    nombre = models.CharField(max_length=200)
    
class Ventas(models.Model):
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)