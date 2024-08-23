# Generated by Django 5.0.7 on 2024-08-23 18:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Arriendos_app', '0004_usuario_username'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usuario',
            options={},
        ),
        migrations.AlterModelManagers(
            name='usuario',
            managers=[
            ],
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='apellido',
            new_name='apellidos',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='nombre',
            new_name='nombres',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='email',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='password',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='telefono',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='user_permissions',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='username',
        ),
        migrations.AddField(
            model_name='usuario',
            name='correo_electronico',
            field=models.EmailField(default='default@example.com', max_length=254, unique=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='telefono_personal',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuario',
            name='user',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='usuario',
            name='direccion',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='rut',
            field=models.CharField(max_length=12, unique=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='tipo_usuario',
            field=models.CharField(choices=[('arrendatario', 'Arrendatario'), ('arrendador', 'Arrendador')], default='arrendatario', max_length=20),
        ),
    ]