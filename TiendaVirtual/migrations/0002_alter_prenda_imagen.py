# Generated by Django 5.0.6 on 2024-07-12 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TiendaVirtual', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prenda',
            name='imagen',
            field=models.ImageField(upload_to='media/'),
        ),
    ]
