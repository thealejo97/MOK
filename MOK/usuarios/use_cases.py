from MOK.usuarios.models import Usuario

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
    def execute(self):
        usuarios = Usuario.objects.all()
        return usuarios

class BorrarUsuarioUseCase:
    print("borrando caso uso")
    def execute(self, pk):
        try:
            usuario = Usuario.objects.get(pk=pk)
            usuario.delete()
            print("borrandoo")
            return True
        except Usuario.DoesNotExist:
            return False