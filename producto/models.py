from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.TextField(max_length=100)
    descripcion = models.TextField(max_length=300)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    modelo = models.TextField(max_length=100)
    marca = models.TextField(max_length=100)
    codigo = models.IntegerField()
    stock = models.IntegerField()

    def __str__(self):
        return self.nombre