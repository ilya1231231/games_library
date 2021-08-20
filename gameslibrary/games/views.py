from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View

from .models import Game


class GameView(View):

    def get(self, request):
        games = Game.objects.all()
        return render(request, 'games/game_table.html', {'game_list':games})
