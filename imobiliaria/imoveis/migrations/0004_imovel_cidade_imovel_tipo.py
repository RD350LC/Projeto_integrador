# Generated by Django 5.2 on 2025-04-19 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imoveis', '0003_favorito_imagemimovel'),
    ]

    operations = [
        migrations.AddField(
            model_name='imovel',
            name='cidade',
            field=models.CharField(default='Default City', max_length=100),
        ),
        migrations.AddField(
            model_name='imovel',
            name='tipo',
            field=models.CharField(choices=[('Casa', 'Casa'), ('Apartamento', 'Apartamento'), ('Comercial', 'Comercial')], default='Casa', max_length=50),
        ),
    ]
