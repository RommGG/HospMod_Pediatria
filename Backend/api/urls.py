from django.urls import path, include
from rest_framework import routers
from api import views


# Define un enrutador
router = routers.DefaultRouter()
router.register(r'nacimientos', views.BebeViewSet)
router.register(r'partos', views.NacimientosGeneroViewSet, basename='nacimientos_genero')
router.register(r'nciudad', views.NacimientosCiudadViewSet, basename='nacimientos_ciudad')
router.register(r'mongo', views.MongoView, basename='item')
router.register(r'consulta', views.ConsultaMongoViewSet, basename='consulta_mongo')
router.register(r'pacientes', views.ConsultaMongoGrafica1, basename='consulta_grafica')
router.register(r'pacientes2', views.ConsultaMongoGrafica2, basename='consulta_grafica2')
urlpatterns = [
    path('api/', include(router.urls)),
]

