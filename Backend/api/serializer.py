from rest_framework import serializers
from .models import nacimientosBebes, SeguimientoPediatrico
# Serializador para ver/obtener información de un bebé
class BebeSerializer(serializers.ModelSerializer):
    class Meta:
        model = nacimientosBebes
        fields = '__all__'

# Serializador para crear/actualizar información de un bebé
class BebeCrearSerializer(serializers.ModelSerializer):
    class Meta:
        model = nacimientosBebes
        exclude = ['id']  # Excluimos el campo 'id' ya que es autoincremental

# Serializador para ver/obtener información de seguimiento pediátrico
class SeguimientoPediatricoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeguimientoPediatrico
        fields = '__all__'

# Serializador para crear/actualizar información de seguimiento pediátrico
class SeguimientoPediatricoCrearSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeguimientoPediatrico
        exclude = ['id_paciente'] 
  
  