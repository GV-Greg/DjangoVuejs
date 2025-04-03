from rest_framework import serializers
from .models import Config

class ConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = Config
        fields = ['id', 'fusion', 'active', 'created_at']
        read_only_fields = ['created_at']