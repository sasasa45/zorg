# Generated by Django 3.0.3 on 2020-07-06 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0005_productcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcode',
            name='code',
            field=models.CharField(max_length=8, unique=True),
        ),
    ]