# Generated by Django 4.1 on 2022-10-17 21:29

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app1', '0005_rename_avatares_avatars'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Avatars',
            new_name='Avatar',
        ),
    ]
