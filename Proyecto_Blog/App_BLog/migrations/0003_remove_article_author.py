# Generated by Django 5.0.1 on 2024-01-18 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App_BLog', '0002_avatar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='author',
        ),
    ]