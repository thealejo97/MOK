# from confluent_kafka import Producer
# import json
#
# # Crear una instancia global del productor para reutilizarla en diferentes llamadas
# producer = Producer({'bootstrap.servers': 'localhost:9092'})
#
# def solicitar_crear_detallepedido_broker(request, pedido_id, producto_id, cantidad):
#     mensaje = {
#         'pedido_id': pedido_id,
#         'producto_id': producto_id,
#         'cantidad': cantidad,
#     }
#     producer.produce('pedido-creado', value=json.dumps(mensaje).encode('utf-8'))
#     producer.flush()