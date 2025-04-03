from django.db import models

class Config(models.Model):
    """
    Model to store configuration settings.
    """
    fusion = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Configuration {self.id} - {'Active' if self.active else 'Inactive'}"
    
    class Meta:
        verbose_name = "Configuration"
        verbose_name_plural = "Configurations"
        ordering = ['-created_at']  # Trier par date de création (la plus récente en premier)
        
    @classmethod
    def get_active_config(cls):
        """
        Retourne la configuration active la plus récente
        """
        return cls.objects.filter(active=True).first()