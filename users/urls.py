from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name = 'login'),
    path('logout/', views.logout, name = 'logout'),
    path('profile/', views.profile, name = 'profile'),
    path('domains/tech', views.domains, name = 'domains'),
    path('domains/non-tech', views.domains2, name = 'domains2'),
    path('domains/apply', views.apply, name = 'apply'),
    path('add-task/', views.add_task, name = 'addTask'),

]