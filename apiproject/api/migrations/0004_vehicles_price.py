# Generated by Django 5.0 on 2024-01-07 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_vehicles_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicles',
            name='price',
            field=models.PositiveIntegerField(default=10000),
        ),
    ]
