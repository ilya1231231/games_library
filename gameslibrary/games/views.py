from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from .forms import ReviewForm, RatingForm
from .models import (Game,
                     Category,
                     Company,
                     Genre,
                     Rating)


class GenreYears:
    '''Класс для хранения данных'''

    def get_genre(self):
        return Genre.objects.all()

    def get_year(self):
        return Game.objects.filter(draft=False).values('year')  # Забираем поле years


class GameView(GenreYears, ListView):
    '''Список игр'''
    model = Game
    queryset = Game.objects.filter(draft=False)
    paginate_by = 2

    # def get_context_data(self,*args, **kwargs):
    #     context = super().get_context_data(*args, **kwargs)
    #     context['categories'] = Category.objects.all()
    #     return context


class GameDetailView(GenreYears, DetailView):
    '''Отдельная игра'''
    model = Game
    slug_field = 'url'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['star_form'] = RatingForm
        return context

    # def get(self, request, slug):
    #     game = Game.objects.get(url=slug)
    #     return render(request, 'games/game_detail.html', {'game':game})


class AddReview(GenreYears, View):
    '''Отправка отзывов'''

    def post(self, request, pk):
        form = ReviewForm(request.POST)  # Данные в форме
        game = Game.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)  # Хотим приостановить сохранение перед привязкой к игре
            if request.POST.get('parent', None):  # Ищем в пост запросе ключ parent(Имя нашего поля)
                form.parent_id = int(request.POST.get('parent'))  # достаем значение нашего ключа parent
            form.game = game  # Сохраняем форму в определенную игру
            form.save()
        messages.add_message(request, messages.INFO, 'Ваш отзыв успешно добавлен')
        return redirect(game.get_absolute_url())


class CompanyView(GenreYears, DetailView):
    model = Company
    template_name = 'games/company.html'
    slug_field = 'name'  # Поле,по которому будем искать компанию


class Search(ListView):

    paginate_by = 3

    def get_queryset(self):
        return Game.objects.filter(title__icontains=self.request.GET.get('search'))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['search'] = self.request.GET.get('search')
        return context


class GameFilter(GenreYears, ListView):
    '''Фильтр игр'''
    paginate_by = 2

    def get_queryset(self):
        queryset = Game.objects.filter(
            Q(year__in=self.request.GET.getlist('year')),
            Q(genre__in=self.request.GET.getlist('genre'))
        ).distinct()  # Убирает повторяющиеся элементы
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['year'] = ''.join(
            [f'year={x}&' for x in self.request.GET.getlist('year')]
        )  # Генерация ссылки на отфильтрованную страницу
        context['genre'] = ''.join(
            [f'genre={x}' for x in self.request.GET.getlist('genre')]
        )
        return context


'''
Фильтрация игр, там,где года будут входить в список, возвращаемого с фронта(список годов)
с помощью метода getlist из GET запроса достаем все значения полей 'year'
'''


class AddStarRating(View):

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def post(self, request):

        form = RatingForm(request.POST)  # когда придет POST запрос, в форму передаем request.POST для генерации формы
        if form.is_valid():
            Rating.objects.update_or_create(
                ip=self.get_client_ip(request),
                game_id=int(request.POST.get('game')),
                defaults={'star_id': int(request.POST.get('star'))}  # Изменяемые поля
            )

            # c = Rating.objects.get(ip=self.get_client_ip(request), game_id=int(request.POST.get('game'))).star
            # print(c)
            return HttpResponse(status=201)
        else:
            return HttpResponse(status=400)

# class RatingScreen(View):
#
#     def get_client_ip(self, request):
#         x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
#         if x_forwarded_for:
#             ip = x_forwarded_for.split(',')[0]
#         else:
#             ip = request.META.get('REMOTE_ADDR')
#         return ip
#
#     ipu = get_client_ip
#     star = Rating.objects.filter(ip=ipu)
