from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Item
from .serializers import ItemSerializer

class ItemViewSet(viewsets.ModelViewSet):
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Filtra los elementos para que el usuario autenticado solo vea los suyos (opcional pero recomendado)
        return Item.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)






""" 
        Como registraste el recurso con el prefijo 'items' y usas un ModelViewSet, el DefaultRouter crea automáticamente las siguientes rutas RESTful:

GET /api/items/ -> Lista todos los elementos (List) o permite crear uno nuevo mediante POST.

GET /api/items/<id>/ -> Obtiene el detalle de un elemento específico (Retrieve), lo actualiza con PUT/PATCH, o lo elimina con DELETE. """