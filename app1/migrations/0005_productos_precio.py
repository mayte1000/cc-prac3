# Generated by Django 4.2.8 on 2023-12-16 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_ventas'),
    ]

    operations = [
        migrations.AddField(
            model_name='productos',
            name='precio',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
