""" Users storage. """

# Django
from django.core.files.storage import FileSystemStorage
from django.conf import settings

# Utils
import os

class OverwriteStorage(FileSystemStorage):
    """ Ensure that profile image are ovewritte,
    each user can only have one picture. """

    def get_available_name(self, name, max_length=None):
        """ If the filename already exists, r
        emove it as if it was a true file system """

        if self.exists(name):
            os.remove(os.path.join(settings.MEDIA_ROOT, name))
        return name