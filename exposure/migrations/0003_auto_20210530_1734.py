# Generated by Django 3.2.3 on 2021-05-30 20:34

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('exposure', '0002_auto_20210524_2118'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exposure',
            name='user',
        ),
        migrations.AddField(
            model_name='exposure',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
