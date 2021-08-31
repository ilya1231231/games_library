from django.urls import path

from.views import GameView, GameDetailView, AddReview, CompanyView



urlpatterns = [
    path('', GameView.as_view()),
    path('<slug:slug>/', GameDetailView.as_view(), name='game_detail'),
    path('review/<int:pk>/', AddReview.as_view(), name='add_review'),
    path('company/<str:slug>/', CompanyView.as_view(), name='company_detail'),

]