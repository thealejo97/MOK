from rest_framework import viewsets, status
from rest_framework.response import Response
from MOK.pedidos.serializers import PedidoSerializer
from MOK.pedidos.use_cases import CrearPedidoUseCase,ObtenerTodosPedidosUseCase,BorrarPedidoUseCase,ObtenerPedidoUseCase

class PedidosViewSet(viewsets.ViewSet):
    """
    ViewSet que permite la creación, listado, y recuperación de pedidos.
    """
    def create(self, request):
        serializer = PedidoSerializer(data=request.data)
        if serializer.is_valid():
            pedido_data = serializer.validated_data
            use_case = CrearPedidoUseCase()
            producto_creado = use_case.execute(pedido_data)
            return Response(status=status.HTTP_201_CREATED, data=PedidoSerializer(producto_creado).data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

    def retrieve(self, request, pk=None):
        use_case = ObtenerPedidoUseCase()
        producto = use_case.execute(pk)
        if producto:
            return Response(status=status.HTTP_200_OK, data=PedidoSerializer(producto).data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        page_number = int(request.query_params.get('page_number', 1))
        page_size = 10
        use_case = ObtenerTodosPedidosUseCase()
        productos = use_case.execute(page_number, page_size)
        serializer = PedidoSerializer(productos, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def delete(self, request, pk=None):
        use_case = BorrarPedidoUseCase()
        borrado_exitoso = use_case.execute(pk)
        if borrado_exitoso:
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)
