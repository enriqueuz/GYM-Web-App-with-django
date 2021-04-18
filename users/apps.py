""" Payment app. """

# Django
from django.apps import AppConfig


class UsersConfig(AppConfig):
    """ Users app config. """
    name = 'users'

    def ready(self):
        import users.signals