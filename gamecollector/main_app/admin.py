from django.contrib import admin
# import models
from .models import Game, Playtime

# Register your models here.
admin.site.register(Game)
admin.site.register(Playtime)
