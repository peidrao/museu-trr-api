# Generated by Django 3.2.3 on 2021-05-22 15:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('exposure', '0002_rename_owner_batch_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batch',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]