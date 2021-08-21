from django.urls import path

from.views import GameView, GameDetailView



urlpatterns = [
    path('', GameView.as_view()),
    path('<slug:slug>/', GameDetailView.as_view(), name='game_detail' )
]