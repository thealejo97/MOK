MOK - Aplicación de Backend generada con Django

Este es el proyecto MOK, una aplicación de backend generada con Django. La estructura del proyecto es la siguiente:

- MOK (directorio raíz del proyecto)
  - MOK (directorio principal de la aplicación)
    - usuarios (directorio relacionado con la gestión de usuarios)
    - productos (directorio relacionado con la gestión de productos)
    - pedidos (directorio relacionado con la gestión de pedidos)
    - detallepedidos (directorio relacionado con la gestión de los detalles de los pedidos)
  - settings (directorio relacionado con la configuración del proyecto)
  - urls (directorio relacionado con las rutas y URLs del proyecto)

Rutas

- GET http://localhost:8000/usuarios/: Obtiene un listado de todos los usuarios registrados.
- GET http://localhost:8000/usuarios/<id>/: Obtiene la información de un usuario específico, identificado por su ID.
- POST http://localhost:8000/usuarios/: Crea un nuevo usuario. Se deben proporcionar los siguientes campos en el cuerpo de la solicitud:
  {
    "username": "Hola",
    "first_name": "Hola",
    "last_name": "Hola",
    "password": "Hola"
  }
- DELETE http://localhost:8000/usuarios/<id>/: Borra un usuario específico, identificado por su ID.

Asegúrate de reemplazar `<id>` con el ID numérico correspondiente al usuario que deseas obtener o borrar.

Ten en cuenta que estas rutas corresponden a la gestión de usuarios en la aplicación. 