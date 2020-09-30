# Generated by Django 3.0.7 on 2020-09-24 12:23

from django.db import migrations, models
import users.models
import users.storage


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200728_1839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.png', storage=users.storage.OverwriteStorage(), upload_to=users.models.profile_path),
        ),
    ]
