from django.contrib import admin
from .models import  Application, Profile, Team, Task


# Register your models here.
admin.site.register(Profile)
admin.site.register(Team)
admin.site.register(Task)
admin.site.register(Application)