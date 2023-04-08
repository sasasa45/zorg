# Generated by Django 3.0.3 on 2020-08-04 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0015_auto_20200716_2313'),
    ]

    operations = [
        migrations.CreateModel(
            name='Spy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=256)),
                ('slug', models.CharField(max_length=256)),
                ('attempts', models.IntegerField()),
            ],
            options={
                'unique_together': {('slug', 'ip')},
            },
        ),
    ]