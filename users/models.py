from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE, PROTECT
from django.db.models.fields.related import OneToOneField



# Create your models here.

class Profile(models.Model):
    user =  models.OneToOneField(User, on_delete=CASCADE, null=True)
    teams = models.ManyToManyField('Team', related_name='team_members')
    def __str__(self):
        return f"{self.user.username}: {self.user.first_name} {self.user.last_name}"


class Team(models.Model):
    team_name = models.CharField(max_length=60, null=True)
    code = models.CharField(max_length=16, null=True)
    desc = models.CharField(max_length=500, null=True)
    img_url = models.URLField(max_length=2000, null=True)
    def __str__(self):
        return f"{self.team_name}"

class Task(models.Model):
    team = models.ForeignKey('Team', on_delete=CASCADE, null=True, related_name="team_tasks")
    task_title = models.CharField(max_length=100)
    task_desc = models.TextField()
    def __str__(self):
        return f"{self.task_title}"

class Application(models.Model):
    user =  models.ForeignKey(User, on_delete=CASCADE, related_name="applied_for")
    team = models.ForeignKey('Team', related_name="appliedTo", on_delete=CASCADE, null=True)
    whyTeam = models.TextField()
    prevExp = models.TextField()

    class Preference(models.IntegerChoices):
        First = 1
        Second = 2
        Third = 3
    preference = models.IntegerField(choices=Preference.choices, null=True)
    expect = models.TextField(null=True)

    def __str__(self):
        return f"{self.user}: {self.team}"

