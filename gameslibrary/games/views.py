
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from .forms import ReviewForm
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


class AddReview(View):
    '''Отправка отзывов'''
    def post(self, request, pk):
        form = ReviewForm(request.POST) #Данные в форме
        game = Game.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)      #Хотим приостановить сохранение перед привязкой к игре
            form.game = game       #Сохраняем форму в определенную игру
            form.save()
        return redirect(game.get_absolute_url())