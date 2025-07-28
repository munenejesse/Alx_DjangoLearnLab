from django.apps import AppConfig


class RelationshipAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'relationship_app'

def ready(self):
    import relationship_app.signals  # assuming you move signal to a separate file
