# Generated by Django 4.1.5 on 2023-01-19 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solid_api', '0003_remove_drinks_imageurls'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drinks',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
