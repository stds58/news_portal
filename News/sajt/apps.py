from django.apps import AppConfig


class SajtConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sajt'

    def ready(self):
        import sajt.signals
