# Generated by Django 3.2.6 on 2021-10-28 13:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0013_alter_application_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='team1',
        ),
        migrations.RemoveField(
            model_name='application',
            name='team2',
        ),
        migrations.RemoveField(
            model_name='application',
            name='team3',
        ),
        migrations.AddField(
            model_name='application',
            name='preference',
            field=models.IntegerField(choices=[(1, 'First'), (2, 'Second'), (3, 'Third')], null=True),
        ),
        migrations.AddField(
            model_name='application',
            name='team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='appliedTo', to='users.team'),
        ),
        migrations.AlterField(
            model_name='application',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applied_for', to=settings.AUTH_USER_MODEL),
        ),
    ]
