from django.apps import AppConfig

class EscholarConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'eScholar'

    def ready(self):
        import eScholar.signals  