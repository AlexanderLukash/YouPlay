from django.apps import AppConfig


class GamelibsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'gamelibs'


class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    # add this
    def ready(self):
        import users.signals  # noqa
