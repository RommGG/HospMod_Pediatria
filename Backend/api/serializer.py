from rest_framework import serializers
from .models import nacimientosBebes, ViewNacimientos, ViewNacimientosCiudad
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
        
        
# Serializador para llamar la view de mysql 
class nacimientosSerializer(serializers.ModelSerializer):
    class Meta:
        model = ViewNacimientos
        fields = '__all__'
        
# Serializador para llamar la view de mysql 
class ciudadNacimientosSerializer(serializers.ModelSerializer):
    class Meta:
        model = ViewNacimientosCiudad
        fields = '__all__'        

#serializer de la consulta de mongo contar el numero pacientes
class ResultadoSerializer(serializers.Serializer):
    pass