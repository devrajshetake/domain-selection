from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name = 'login'),
    path('logout/', views.logout, name = 'logout'),
    path('profile/', views.profile, name = 'profile'),
    path('domains/', views.domains, name = 'domains'),
    path('domains2/', views.domains2, name = 'domains2'),
    path('add-task/', views.add_task, name = 'addTask'),
    path('domains/<str:code>', views.applyTeam, name = 'apply'),

]