# Generated by Django 4.0.3 on 2022-04-11 16:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_protein_protein_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='protein',
            name='protein_slug',
        ),
    ]
