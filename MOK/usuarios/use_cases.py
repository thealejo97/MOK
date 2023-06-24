from MOK.usuarios.models import Usuario
from django.core.paginator import Paginator, EmptyPage

class CrearUsuarioUseCase:
    def execute(self, usuario_data):
        usuario = Usuario.objects.create(
            first_name=usuario_data['first_name'],
            last_name=usuario_data['last_name'],
            password=usuario_data['password'],
        )
        return usuario

class ObtenerUsuarioUseCase:
    def execute(self, pk):
        try:
            usuario = Usuario.objects.get(pk=pk)
            return usuario
        except Usuario.DoesNotExist:
            return None

class ObtenerTodosUsuariosUseCase:
    def execute(self, page_number, page_size):
        usuarios = Usuario.objects.all().order_by('id')
        paginator = Paginator(usuarios, page_size)

        try:
            page = paginator.page(page_number)
            return page.object_list
        except EmptyPage:
            return []
class BorrarUsuarioUseCase:
    def execute(self, pk):
        try:
            usuario = Usuario.objects.get(pk=pk)
            usuario.delete()
            return True
        except Usuario.DoesNotExist:
            return False