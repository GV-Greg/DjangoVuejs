from django.contrib import admin
from .models import Config

@admin.register(Config)
class ConfigAdmin(admin.ModelAdmin):
    list_display = ('id', 'fusion', 'active', 'created_at')
    list_filter = ('active', 'fusion', 'created_at')
    search_fields = ('id',)
    readonly_fields = ('created_at',)
    
    def save_model(self, request, obj, form, change):
        # Si cette configuration est active, désactiver toutes les autres
        if obj.active:
            Config.objects.exclude(pk=obj.pk).update(active=False)
        super().save_model(request, obj, form, change)
