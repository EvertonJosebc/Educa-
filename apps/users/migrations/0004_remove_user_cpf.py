# Generated by Django 4.1.5 on 2023-01-30 04:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_typeuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='cpf',
        ),
    ]