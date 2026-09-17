from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ItemViewSet

router = DefaultRouter()
router.register(r'items', ItemViewSet, basename='item')

urlpatterns = [
    path('', include(router.urls)),
]


""" Como registraste el recurso con el prefijo 'items' y usas un ModelViewSet, el DefaultRouter crea automáticamente las siguientes rutas RESTful:

GET /api/items/ -> Lista todos los elementos (List) o permite crear uno nuevo mediante POST.

GET /api/items/<id>/ -> Obtiene el detalle de un elemento específico (Retrieve), lo actualiza con PUT/PATCH, o lo elimina con DELETE.

Además, el DefaultRouter por defecto genera una página raíz navegable (la interfaz web de DRF) en la ruta raíz (/api/) que te muestra un listado interactivo de todas las URLs disponibles en ese router."""
