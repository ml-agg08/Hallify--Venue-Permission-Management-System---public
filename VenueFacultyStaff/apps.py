from django.apps import AppConfig


class VenuefacultystaffConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'VenueFacultyStaff'

    def ready(self):
        import VenueFacultyStaff.signals