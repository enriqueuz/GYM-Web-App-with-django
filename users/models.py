from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import os
from users.storage import OverwriteStorage


def profile_path(instance, filename):
    file_extension = filename.split('.')[-1]
    image_path = f'profile_pics/{instance.user.username}_profile.{file_extension}'
    return image_path


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', storage=OverwriteStorage(), upload_to=profile_path)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


