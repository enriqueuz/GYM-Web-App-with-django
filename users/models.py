""" Users models. """

# Django
from django.db import models
from django.contrib.auth.models import User

# Utils
from PIL import Image
import os

# Storage
from users.storage import OverwriteStorage


def profile_path(instance, filename):
    """ Return path for profile image. """

    file_extension = filename.split('.')[-1]
    image_path = f'profile_pics/{instance.user.username}_profile.{file_extension}'

    return image_path


class Profile(models.Model):
    """ Profile model. """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', storage=OverwriteStorage(), upload_to=profile_path)

    def __str__(self):
        """ Return user's name. """
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        """ Override de save method to resize images. """
        
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


