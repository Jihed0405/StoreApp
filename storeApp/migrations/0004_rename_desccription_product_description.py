# Generated by Django 4.1.7 on 2023-04-02 20:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storeApp', '0003_add_slug_to_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='desccription',
            new_name='description',
        ),
    ]
