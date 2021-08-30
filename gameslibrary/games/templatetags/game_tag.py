from django import template
from ..models import Category, Game

'''Тэг для просмотра всех категорий'''
register = template.Library()


@register.simple_tag()
def get_categories():
    return Category.objects.all()


@register.inclusion_tag('games/tags/new_added_games.html')  # Для рендера в шаблоне inclusion
def get_new_games(count=5):  # Аргумент по умолчанию
    games = Game.objects.order_by('id')[:count]  # Ставлю очередь по id
    return {'new_games': games}
