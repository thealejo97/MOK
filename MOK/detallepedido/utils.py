# from kafka import KafkaConsumer
# import json
#
# from MOK.detallepedido.models import DetallePedido
# from MOK.pedido.models import Pedido
#
# def recibir_solicitud_crear_detallepedido_broker():
#     consumer = KafkaConsumer('pedido-creado', bootstrap_servers='localhost:9092')
#     print("Recibiendo broker pedido")
#     for mensaje in consumer:
#         print(mensaje)
#         mensaje = json.loads(mensaje.value.decode('utf-8'))
#         pedido_id = int(mensaje['pedido_id'])
#         producto_id = int(mensaje['producto_id'])
#         cantidad = int(mensaje['cantidad'])
#
#         pedido = Pedido.objects.get(id=pedido_id)
#
#         if pedido:
#             DetallePedido.objects.create(
#                 pedido=pedido,
#                 producto_id=producto_id,
#                 cantidad=cantidad
#             )