# Generated by Django 3.2.6 on 2021-10-26 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20211026_2011'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='team',
        ),
        migrations.AddField(
            model_name='application',
            name='team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='appliedTo', to='users.team'),
        ),
    ]
