# Generated by Django 5.0.1 on 2024-01-22 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_BLog', '0014_article_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avatar',
            name='image',
            field=models.ImageField(blank=True, default='avatar.webp', null=True, upload_to='avatars'),
        ),
    ]
