from django.db import models

class Producto(models.Model):
    """
    Clase producto cada producto tiene un nombre y un precio
    """
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField()