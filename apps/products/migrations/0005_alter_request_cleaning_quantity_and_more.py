# Generated by Django 4.1.5 on 2023-01-16 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_rename_type_food_typecategoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request_cleaning',
            name='quantity',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='request_food',
            name='quantity',
            field=models.FloatField(blank=True, null=True),
        ),
    ]