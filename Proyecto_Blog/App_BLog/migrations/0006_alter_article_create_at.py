# Generated by Django 5.0.1 on 2024-01-19 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_BLog', '0005_rename_body_article_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='create_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]