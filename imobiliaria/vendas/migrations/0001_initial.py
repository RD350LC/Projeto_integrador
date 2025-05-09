# Generated by Django 5.2 on 2025-04-15 23:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clientes', '0001_initial'),
        ('corretores', '0001_initial'),
        ('imoveis', '0002_caracteristicas_endereco_alter_imovel_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_venda', models.DateField()),
                ('valor_venda', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.cliente')),
                ('corretor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='corretores.corretor')),
                ('imovel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imoveis.imovel')),
            ],
        ),
    ]
