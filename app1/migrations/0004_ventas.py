# Generated by Django 4.2.8 on 2023-12-15 19:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_rename_clientesproductos_clientes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ventas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.clientes')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.productos')),
            ],
        ),
    ]
