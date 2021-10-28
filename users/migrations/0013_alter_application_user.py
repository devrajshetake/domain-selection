# Generated by Django 3.2.6 on 2021-10-28 13:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0012_auto_20211028_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='applied_for', to=settings.AUTH_USER_MODEL),
        ),
    ]
