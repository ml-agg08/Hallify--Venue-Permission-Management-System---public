from django.apps import AppConfig

class FacultycoordinatorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'FacultyCoordinator'

    def ready(self):
        import FacultyCoordinator.signals
