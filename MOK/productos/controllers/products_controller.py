from rest_framework import viewsets, status
from rest_framework.response import Response
from MOK.productos.serializers import ProductoSerializer
from MOK.productos.use_cases import CrearProductoUseCase, ObtenerProductoUseCase, ObtenerTodosProductosUseCase, BorrarProductoUseCase

class ProductosViewSet(viewsets.ViewSet):
    """
    ViewSet que permite la creación, listado, y recuperación de productos.
    """
    def create(self, request):
        serializer = ProductoSerializer(data=request.data)
        if serializer.is_valid():
            producto_data = serializer.validated_data
            use_case = CrearProductoUseCase()
            producto_creado = use_case.execute(producto_data)
            return Response(status=status.HTTP_201_CREATED, data=ProductoSerializer(producto_creado).data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

    def retrieve(self, request, pk=None):
        use_case = ObtenerProductoUseCase()
        producto = use_case.execute(pk)
        if producto:
            return Response(status=status.HTTP_200_OK, data=ProductoSerializer(producto).data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        page_number = int(request.query_params.get('page_number', 1))
        page_size = 10
        use_case = ObtenerTodosProductosUseCase()
        productos = use_case.execute(page_number, page_size)
        serializer = ProductoSerializer(productos, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def delete(self, request, pk=None):
        use_case = BorrarProductoUseCase()
        borrado_exitoso = use_case.execute(pk)
        if borrado_exitoso:
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)
