# Generated by Django 4.1 on 2022-10-17 20:49

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app1', '0003_avatar'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Avatar',
            new_name='Avatares',
        ),
    ]
