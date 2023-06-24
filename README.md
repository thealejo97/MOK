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
* Usuarios:
- GET http://localhost:8000/usuarios/: Obtiene un listado de todos los usuarios registrados.
- GET http://localhost:8000/usuarios/?page_number=2: Obtiene un listado de los usuarios paginados por 10, si existe en la pagina
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

* Productos
- GET http://localhost:8000/productos/: Obtiene un listado de todos los productos registrados. Los productos se retornan paginados, usando la paginacion de Django, esta retorna los productos paginados de a 10 productos por pagina
- GET http://localhost:8000/productos/?page_number=2: Obtiene un listado de los productos paginados por 10, si existe en la pagina
- GET http://localhost:8000/productos/<id>/: Obtiene la información de un producto específico, identificado por su ID.
- POST http://localhost:8000/productos/: Crea un nuevo producto. Se deben proporcionar los siguientes campos en el cuerpo de la solicitud:
  {
    "nombre": "str",
    "precio": "str"
  }
- DELETE http://localhost:8000/productos/<id>/: Borra un usuario específico, identificado por su ID.

Asegúrate de reemplazar `<id>` con el ID numérico correspondiente al usuario que deseas obtener o borrar.

* Pedido
- GET http://localhost:8000/pedidos/: Obtiene un listado de todos los pedidos registrados. Los pedidos se retornan paginados, usando la paginacion de Django, esta retorna los pedidos paginados de a 10 pedidos por pagina
- GET http://localhost:8000/pedidos/?page_number=2: Obtiene un listado de los pedidos paginados por 10, si existe en la pagina
- GET http://localhost:8000/pedidos/<id>/: Obtiene la información de un usuario específico, identificado por su ID.
- POST http://localhost:8000/pedidos/: Crea un nuevo pedido. Se deben proporcionar los siguientes campos en el cuerpo de la solicitud:
  {
    "usuario": "str",
    "fecha": "date"
  }
- DELETE http://localhost:8000/pedidos/<id>/: Borra un pedido específico, identificado por su ID.

Asegúrate de reemplazar `<id>` con el ID numérico correspondiente al usuario que deseas obtener o borrar.
