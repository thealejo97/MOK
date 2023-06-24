from rest_framework import serializers
from MOK.detallepedido.models import DetallePedido

class DetallePedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetallePedido
        fields = '__all__'