# Generated by Django 3.0.3 on 2020-07-06 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0013_photos_description_ua'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photos',
            name='description_ua',
            field=models.TextField(blank=True, null=True),
        ),
    ]
