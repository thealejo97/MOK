from MOK.productos.models import Producto

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
    def execute(self):
        productos = Producto.objects.all()
        return productos

class BorrarProductoUseCase:
    def execute(self, pk):
        try:
            producto = Producto.objects.get(pk=pk)
            producto.delete()
            return True
        except Producto.DoesNotExist:
            return False
