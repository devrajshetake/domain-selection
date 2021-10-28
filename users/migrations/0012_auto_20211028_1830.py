# Generated by Django 3.2.6 on 2021-10-28 13:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20211028_0817'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='preference',
        ),
        migrations.RemoveField(
            model_name='application',
            name='team',
        ),
        migrations.AddField(
            model_name='application',
            name='team1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='appliedTo1', to='users.team'),
        ),
        migrations.AddField(
            model_name='application',
            name='team2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='appliedTo2', to='users.team'),
        ),
        migrations.AddField(
            model_name='application',
            name='team3',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='appliedTo3', to='users.team'),
        ),
    ]
