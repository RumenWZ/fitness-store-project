# Generated by Django 4.0.3 on 2022-04-13 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_sales_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sales',
            old_name='product',
            new_name='product_id',
        ),
    ]