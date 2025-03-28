from django.apps import AppConfig


class OfficeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Office'

    def ready(self):
        import Office.signals