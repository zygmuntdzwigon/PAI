# Generated by Django 3.0.2 on 2020-01-12 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_moderator',
            field=models.BooleanField(default=False),
        ),
    ]
