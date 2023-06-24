from django.db import models

from MOK.pedidos.models import Pedido
from MOK.productos.models import Producto


class DetallePedido(models.Model):
    """
    Modelo que relaciona una compra(pedido) con un usuario
    """
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()