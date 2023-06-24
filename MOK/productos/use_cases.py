from MOK.productos.models import Producto
from django.core.paginator import Paginator, EmptyPage

class CrearProductoUseCase:
    def execute(self, producto_data):
        producto = Producto.objects.create(
            nombre=producto_data['nombre'],
            precio=producto_data['precio'],
        )
        return producto

class ObtenerProductoUseCase:
    def execute(self, pk):
        try:
            producto = Producto.objects.get(pk=pk)
            return producto
        except Producto.DoesNotExist:
            return None

class ObtenerTodosProductosUseCase:
    def execute(self, page_number, page_size):
        productos = Producto.objects.all().order_by('id')
        paginator = Paginator(productos, page_size)

        try:
            page = paginator.page(page_number)
            return page.object_list
        except EmptyPage:
            return []
class BorrarProductoUseCase:
    def execute(self, pk):
        try:
            producto = Producto.objects.get(pk=pk)
            producto.delete()
            return True
        except Producto.DoesNotExist:
            return False
