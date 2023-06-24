MOK - Aplicación de Backend generada con Django

Este es el proyecto MOK, una aplicación de backend generada con Django. La estructura del proyecto es la siguiente:

El proyecto cuenta con 4 tablas relacionadas entre sí:

- usuario
- producto
- pedido (relación con usuario)
- detallepedido (relación con pedido)

Se utiliza el ORM de Django para gestionar las relaciones y se utiliza una base de datos SQLite3 (para efectos de practicidad, se incluye en el repositorio de Git).

Estructura del proyecto:

- MOK (directorio raíz del proyecto)
  - MOK (directorio principal de la aplicación)
    - usuarios (directorio relacionado con la gestión de usuarios)
    - productos (directorio relacionado con la gestión de productos)
    - pedidos (directorio relacionado con la gestión de pedidos)
    - detallepedidos (directorio relacionado con la gestión de los detalles de los pedidos)
  - settings (directorio relacionado con la configuración del proyecto)
  - urls (directorio relacionado con las rutas y URLs del proyecto)

Rutas:

- GET http://localhost:8000/usuarios/: Obtiene un listado de todos los usuarios registrados.
- GET http://localhost:8000/usuarios/<id>/: Obtiene la información de un usuario específico, identificado por su ID.
- POST http://localhost:8000/usuarios/: Crea un nuevo usuario. Se deben proporcionar los siguientes campos en el cuerpo de la solicitud:
  {
    "username": "str",
    "first_name": "str",
    "last_name": "str",
    "password": "str"
  }
- DELETE http://localhost:8000/usuarios/<id>/: Borra un usuario específico, identificado por su ID.

Asegúrate de reemplazar `<id>` con el ID numérico correspondiente al usuario que deseas obtener o borrar.
