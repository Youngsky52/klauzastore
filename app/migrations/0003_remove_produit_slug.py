# Generated by Django 4.2 on 2023-04-30 22:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_produit_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produit',
            name='slug',
        ),
    ]