from MOK.detallepedido.models import DetallePedido
from django.core.paginator import Paginator, EmptyPage

class CrearDetallePedidoUseCase:
    def execute(self, detallepedido_data):
        detallepedido = DetallePedido.objects.create(
            pedido=detallepedido_data['pedido'],
            producto=detallepedido_data['producto'],
            cantidad=detallepedido_data['cantidad']
        )
        return detallepedido

class ObtenerDetallePedidoUseCase:
    def execute(self, pk):
        try:
            detallepedido = DetallePedido.objects.get(pk=pk)
            return detallepedido
        except DetallePedido.DoesNotExist:
            return None

class ObtenerTodosDetallePedidosUseCase:
    def execute(self, page_number, page_size):
        detallepedido = DetallePedido.objects.all().order_by('id')
        paginator = Paginator(detallepedido, page_size)

        try:
            page = paginator.page(page_number)
            return page.object_list
        except EmptyPage:
            return []
class BorrarDetallePedidoUseCase:
    def execute(self, pk):
        try:
            detallepedido = DetallePedido.objects.get(pk=pk)
            detallepedido.delete()
            return True
        except DetallePedido.DoesNotExist:
            return False
