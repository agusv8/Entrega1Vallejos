# Generated by Django 4.1 on 2022-09-26 21:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='empleados',
            old_name='cargo',
            new_name='cargos',
        ),
    ]