# Generated by Django 5.1.4 on 2025-01-31 07:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_remove_product_champu_delete_champu'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='color_variant',
            new_name='color_variants',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='size_variant',
            new_name='size_variants',
        ),
    ]
