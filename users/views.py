from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as login_User, logout as logout_User
from django.urls import reverse
from .models import *


# Create your views here.

def home(request):
    context = {'title': "Home"}
    return render(request, "users/index.html", context)

def login(request):
    if request.method == 'POST':
        username = request.POST['username']    
        password = request.POST['password']
        user =  authenticate(request, username=username, password=password)
        if user is not None:
            login_User(request, user)
            return redirect(reverse("domains"))
        else:
            return render(request, 'users/login.html', {'message': "Invalid Credentials!"})
    
    return render(request, 'users/login.html')

def logout(request):
    logout_User(request)
    return redirect(reverse("home"))
    

def domains(request):
    context = {'title': "Domains"}
    return render(request, "users/domains1.html", context)

def domains2(request):
    context = {'title': "Domains"}
    return render(request, "users/nontech.html", context)

def profile(request):
    if not request.user.is_authenticated:
        return redirect(reverse("login"))
    
    profile = Profile.objects.get(user = request.user)
    teams = profile.teams.all()
    context = {'title': 'Profile', 'teams':teams}
    return render(request, "users/profile.html", context)

def add_task(request):
    context = {'title': 'Add Task'}
    if request.method == 'POST':
        taskTitle = request.POST['taskTitle']
        tascDesc = request.POST['taskDesc']
        team = Team.objects.filter(team_name = 'App Development').first()
        print(team)

        inst = Task(team = team, task_title = taskTitle, task_desc = tascDesc)
        inst.save()
        context = {'title': 'Add Task', 'success' : True}
    return render(request, "users/add_task.html", context)

def applyTeam(request, code):
    team = Team.objects.get(code = code)
    tasks = team.team_tasks.all()
    context = {'title':"Apply Now", 'team':team, 'tasks':tasks}
    return render(request, 'users/apply.html', context)