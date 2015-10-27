from django.views.generic import View
from django.views.generic.detail import SingleObjectMixin
from django.shortcuts import render
from games.models import Game


class GameView(SingleObjectMixin, View):
    model = Game
    slug_field = 'sname'
    slug_url_kwarg = 'game_sname'

    def get(self, request, *args, **kwargs):
        return render(request, self.get_object().template_path)