# Generated by Django 5.0.7 on 2024-08-23 19:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Arriendos_app', '0005_alter_usuario_options_alter_usuario_managers_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='correo_electronico',
        ),
        migrations.AddField(
            model_name='contacto',
            name='arrendatario',
            field=models.ForeignKey(default='', limit_choices_to={'tipo_usuario': 'arrendatario'}, on_delete=django.db.models.deletion.CASCADE, to='Arriendos_app.usuario'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inmueble',
            name='arrendador',
            field=models.ForeignKey(default='', limit_choices_to={'tipo_usuario': 'arrendador'}, on_delete=django.db.models.deletion.CASCADE, to='Arriendos_app.usuario'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inmueble',
            name='imagen_url',
            field=models.URLField(blank=True, default='', null=True),
        ),
        migrations.AddField(
            model_name='inmueble',
            name='region',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Arriendos_app.region'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuario',
            name='email',
            field=models.EmailField(default='', max_length=254, unique=True),
            preserve_default=False,
        ),
    ]
