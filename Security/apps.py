from django.apps import AppConfig


class SecurityConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Security'

    def ready(self):
        import Security.signals