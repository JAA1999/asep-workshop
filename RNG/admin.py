from django.contrib import admin
from RNG.models import User, Game
from django.contrib.auth.models import User, Group




# Register your models here.

admin.site.register(User)
admin.site.register(Game)