# Generated by Django 3.0.3 on 2020-07-06 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0010_auto_20200706_2109'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcode',
            name='description_ua',
            field=models.TextField(blank=True, null=True),
        ),
    ]