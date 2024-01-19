# Generated by Django 5.0.1 on 2024-01-17 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('subtitle', models.CharField(max_length=90)),
                ('body', models.TextField(max_length=250)),
                ('author', models.CharField(max_length=50)),
                ('date', models.DateTimeField()),
            ],
        ),
    ]
