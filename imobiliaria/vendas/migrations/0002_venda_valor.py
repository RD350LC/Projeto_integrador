# Generated by Django 5.2 on 2025-04-20 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='venda',
            name='valor',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
