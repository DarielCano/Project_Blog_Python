# Generated by Django 5.0.1 on 2024-01-21 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_BLog', '0008_alter_article_create_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='create_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
