from django.apps import AppConfig

class PullgerAuthConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pullgerAuthJWT'
    multisessionManager = None