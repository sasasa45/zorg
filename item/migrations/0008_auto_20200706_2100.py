# Generated by Django 3.0.3 on 2020-07-06 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0007_items_language'),
    ]

    operations = [
        migrations.RenameField(
            model_name='items',
            old_name='description',
            new_name='description_ru',
        ),
    ]
