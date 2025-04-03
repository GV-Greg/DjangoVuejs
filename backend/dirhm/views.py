from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Config
from .serializers import ConfigSerializer

@api_view(['GET', 'POST'])
def config(request):
    """
    GET: Récupère la configuration active
        - Retourne 404 si aucune configuration n'existe
    POST: Crée une nouvelle configuration active et désactive les autres
    """
    if request.method == 'GET':
        # Récupérer la configuration active la plus récente
        config = Config.objects.filter(active=True).order_by('-created_at').first()
        if config:
            serializer = ConfigSerializer(config)
            return JsonResponse(serializer.data, status=200)
        else:
            return JsonResponse({"detail": "Aucune configuration active trouvée."},status=404)
    
    elif request.method == 'POST':
        # Créer une nouvelle configuration
        serializer = ConfigSerializer(data=request.data)
        if serializer.is_valid():
            # Désactiver toutes les configurations existantes
            Config.objects.all().update(active=False)
            
            # Créer la nouvelle configuration (active par défaut)
            config = serializer.save(active=True)
            
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)