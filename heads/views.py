from django.shortcuts import render
from users.models import *

# Create your views here.

def applied(request, team_code):
    team = Team.objects.get(code = team_code)
    applications = Application.objects.filter(team = team).order_by('user')
    teamprefs = applications.first().user.applied_for.all().order_by('-preference')
    context = {'team':team, 'applications':applications, }
    return render(request, "heads/applied.html", context)