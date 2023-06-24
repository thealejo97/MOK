from django.db import models

from MOK.usuarios.models import Usuario


class Pedido(models.Model):
    """
    Modelo que genera una compra, los detalles de la compra estan en el modelo DetallePedido
    """
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha = models.DateField()