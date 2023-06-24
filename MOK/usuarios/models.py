from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    """
    Modelo de usuario personalizado que hereda de la clase AbstractUser
    de Django para traer todos los atributos del user por defecto de django
    """

    def __str__(self):
        return self.username