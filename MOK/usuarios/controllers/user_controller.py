from rest_framework import viewsets, status
from rest_framework.response import Response
from MOK.usuarios.serializers import UsuarioSerializer
from MOK.usuarios.use_cases import CrearUsuarioUseCase, ObtenerUsuarioUseCase, ObtenerTodosUsuariosUseCase, BorrarUsuarioUseCase

class UsuarioViewSet(viewsets.ViewSet):

    """
    View set que permite la creacion listado y retrive de los usuarios
    """
    def create(self, request):
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            usuario_data = serializer.validated_data
            use_case = CrearUsuarioUseCase()
            usuario_creado = use_case.execute(usuario_data)
            return Response(status=status.HTTP_201_CREATED, data=UsuarioSerializer(usuario_creado).data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

    def retrieve(self, request, pk=None):
        print("aca no se por que")
        use_case = ObtenerUsuarioUseCase()
        usuario = use_case.execute(pk)
        if usuario:
            return Response(status=status.HTTP_200_OK, data=UsuarioSerializer(usuario).data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        page_number = int(request.query_params.get('page_number', 1))
        page_size = 10
        use_case = ObtenerTodosUsuariosUseCase()
        usuarios = use_case.execute(page_number,page_size)
        serializer = UsuarioSerializer(usuarios, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def delete(self, request, pk=None):
        print("aca 1")
        use_case = BorrarUsuarioUseCase()
        borrado_exitoso = use_case.execute(pk)
        if borrado_exitoso:
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)