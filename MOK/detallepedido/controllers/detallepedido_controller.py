from rest_framework import viewsets, status
from rest_framework.response import Response
from MOK.detallepedido.serializers import DetallePedidoSerializer
from MOK.detallepedido.use_cases import CrearDetallePedidoUseCase,ObtenerTodosDetallePedidosUseCase,BorrarDetallePedidoUseCase,ObtenerDetallePedidoUseCase

class DetallePedidosViewSet(viewsets.ViewSet):
    """
    ViewSet que permite la creación, listado, y recuperación de pedidos.
    """
    def create(self, request):
        serializer = DetallePedidoSerializer(data=request.data)
        if serializer.is_valid():
            pedido_data = serializer.validated_data
            use_case = CrearDetallePedidoUseCase()
            producto_creado = use_case.execute(pedido_data)
            return Response(status=status.HTTP_201_CREATED, data=DetallePedidoSerializer(producto_creado).data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

    def retrieve(self, request, pk=None):
        use_case = ObtenerDetallePedidoUseCase()
        producto = use_case.execute(pk)
        if producto:
            return Response(status=status.HTTP_200_OK, data=DetallePedidoSerializer(producto).data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        page_number = int(request.query_params.get('page_number', 1))
        page_size = 10
        use_case = ObtenerTodosDetallePedidosUseCase()
        productos = use_case.execute(page_number, page_size)
        serializer = DetallePedidoSerializer(productos, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def delete(self, request, pk=None):
        use_case = BorrarDetallePedidoUseCase()
        borrado_exitoso = use_case.execute(pk)
        if borrado_exitoso:
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)
