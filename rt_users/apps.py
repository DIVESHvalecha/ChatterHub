from django.apps import AppConfig


class RtUsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'rt_users'
    
    def ready(self):
        # Import signals to ensure they are registered when the app is ready
        import rt_users.signals
