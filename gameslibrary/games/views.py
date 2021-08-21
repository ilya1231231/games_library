
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from .models import Game


class GameView(ListView):
    '''Список игр'''
    model = Game
    queryset = Game.objects.filter(draft=False)
    # template_name = 'games/game_table.html'



class GameDetailView(DetailView):
    '''Отдельная игра'''
    model = Game
    slug_field = 'url'

    # def get(self, request, slug):
    #     game = Game.objects.get(url=slug)
    #     return render(request, 'games/game_detail.html', {'game':game})