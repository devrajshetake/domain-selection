from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('heads/<str:team_code>/applications', views.applied, name='applied'),
]
