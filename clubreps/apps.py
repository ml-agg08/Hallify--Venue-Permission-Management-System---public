from django.apps import AppConfig


class ClubrepsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'clubreps'

    def ready(self):
        import clubreps.signals