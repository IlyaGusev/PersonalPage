from django.contrib import admin
from games.models import Game


class GameAdmin(admin.ModelAdmin):
    model = Game
    list_display = ['sname']

admin.site.register(Game, GameAdmin)