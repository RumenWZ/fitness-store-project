# Generated by Django 4.0.3 on 2022-04-11 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='protein',
            name='protein_slug',
            field=models.TextField(default=''),
        ),
    ]
