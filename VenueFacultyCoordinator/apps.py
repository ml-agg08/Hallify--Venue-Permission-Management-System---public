from django.apps import AppConfig

class VenuefacultycoordinatorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'VenueFacultyCoordinator'

    def ready(self):
        import VenueFacultyCoordinator.signals
