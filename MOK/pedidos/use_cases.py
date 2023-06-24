from MOK.pedidos.models import Pedido
from django.core.paginator import Paginator, EmptyPage

class CrearPedidoUseCase:
    def execute(self, pedido_data):
        pedido = Pedido.objects.create(
            usuario=pedido_data['usuario'],
            fecha=pedido_data['fecha'],
        )
        return pedido

class ObtenerPedidoUseCase:
    def execute(self, pk):
        try:
            producto = Pedido.objects.get(pk=pk)
            return producto
        except Pedido.DoesNotExist:
            return None

class ObtenerTodosPedidosUseCase:
    def execute(self, page_number, page_size):
        productos = Pedido.objects.all().order_by('id')
        paginator = Paginator(productos, page_size)

        try:
            page = paginator.page(page_number)
            return page.object_list
        except EmptyPage:
            return []
class BorrarPedidoUseCase:
    def execute(self, pk):
        try:
            producto = Pedido.objects.get(pk=pk)
            producto.delete()
            return True
        except Pedido.DoesNotExist:
            return False
