from rest_framework import viewsets, status
from .models import nacimientosBebes, ViewNacimientos, ViewNacimientosCiudad
from .serializer import BebeSerializer, BebeCrearSerializer, nacimientosSerializer, ciudadNacimientosSerializer
from rest_framework.response import Response
from bson import ObjectId
from pymongo import MongoClient
from django.conf import settings
import json

client = MongoClient(settings.MONGO_URI)
collection = client[settings.MONGO_DBNAME]['pacientes']

# vista para el modelo nacimientosBebes


class BebeViewSet(viewsets.ModelViewSet):
    queryset = nacimientosBebes.objects.all()
    serializer_class = BebeSerializer

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'update':
            return BebeCrearSerializer
        return BebeSerializer


class NacimientosGeneroViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = ViewNacimientos.objects.raw(
            "SELECT * FROM bd_hospital_210538.vw_nacimientos_genero")
        serializer = nacimientosSerializer(queryset, many=True)
        return Response(serializer.data)


class NacimientosCiudadViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = ViewNacimientosCiudad.objects.raw(
            "SELECT * FROM bd_hospital_210538.vw_nacimientos_por_ciudad;")
        serializer = ciudadNacimientosSerializer(queryset, many=True)
        return Response(serializer.data)


class MongoView(viewsets.ViewSet):

    # metodo para obtener los datos de los pacientes en seguimiento pediatrico
    def list(self, request):
        items = list(collection.find())
        for item in items:
            item['_id'] = str(item['_id'])
        return Response(items)

    # metodo para crear un nuevo seguimiento
    def create(self, request):
        data = json.loads(request.body)
        item_id = collection.insert_one(data).inserted_id
        return Response({'id': str(item_id)}, status=201)

    # Metodo para obtener un paciente en especifico por medio de su id
    def retrieve(self, request, pk=None):
        item = collection.find_one({'_id': ObjectId(pk)})
        if item:
            item['_id'] = str(item['_id'])
            return Response(item)
        else:
            return Response({'error': 'Elemento no encontrado'}, status=404)

    # Metodo para actualizar un paciente en especifico por medio de su id
    def update(self, request, pk=None):
        data = json.loads(request.body)
        result = collection.update_one({'_id': ObjectId(pk)}, {'$set': data})
        if result.modified_count == 1:
            return Response({'message': 'Elemento actualizado correctamente'})
        else:
            return Response({'error': 'Elemento no encontrado'}, status=404)

    # metodo para eliminar expedientes por medio del id
    def destroy(self, request, pk=None):
        try:
            obj_id = ObjectId(pk)
            result = collection.delete_one({'_id': obj_id})
            if result.deleted_count == 1:
                return Response({'message': 'Elemento eliminado correctamente'})
            else:
                return Response({'error': 'Elemento no encontrado'}, status=404)
        except Exception as e:
            return Response({'error': str(e)}, status=500)


class ConsultaMongoViewSet(viewsets.ViewSet):
    def list(self, request):
        try:
            # Realizar la consulta para obtener la cantidad de documentos
            cantidad = collection.count_documents({})
            # Retornar la cantidad como un diccionario
            return Response({'cantidad_pacientes': cantidad}, status=status.HTTP_200_OK)
        except Exception as e:
            # Manejar cualquier error que pueda ocurrir durante la consulta
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ConsultaMongoGrafica2(viewsets.ViewSet):
    def list(self, request):
        try:
            pacientes = collection.aggregate([
                {
                    "$group": {
                        "_id": "$sexo",  # Agrupar por el campo "sexo"
                        "count": {"$sum": 1}  
                    }
                }
            ])
            return Response(pacientes, status=status.HTTP_200_OK)
        except Exception as e:
            # Handle any error that may occur during the query
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




class ConsultaMongoGrafica1(viewsets.ViewSet):
    def list(self, request):
        try:
            # Realizar la consulta para obtener los pacientes
            pacientes = collection.aggregate([
                {
                    # Asegúrate de que exista la fecha de nacimiento
                    "$match": {"fecha_nacimiento": {"$exists": True}}
                },
                {"$group": {"_id": {"year": {"$year": {"$dateFromString": {"dateString": "$fecha_nacimiento"}}}}, "personas_count": {"$sum": 1}}  # Contar la cantidad de personas nacidas por año
                 },
                {
                    "$project": {
                        "_id": 0,  # Excluir el campo _id del resultado
                        "year": "$_id.year",  # Renombrar el campo _id.year como year
                        "personas_count": 1  # Incluir el campo personas_count en el resultado
                    }
                },
                {
                    "$sort": {"year": 1}  # Ordenar los resultados por año
                }
            ])
            # Retornar la lista de pacientes como un diccionario
            return Response(pacientes, status=status.HTTP_200_OK)
        except Exception as e:
            # Manejar cualquier error que pueda ocurrir durante la consulta
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
