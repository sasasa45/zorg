# Generated by Django 3.0.3 on 2020-07-05 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0003_items_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='pdf',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
