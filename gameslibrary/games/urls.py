from django.urls import path

from .views import (GameView,
                    GameDetailView,
                    AddReview,
                    CompanyView,
                    GameFilter,
                    AddStarRating
                    )

urlpatterns = [
    path('', GameView.as_view()),
    path('filter/', GameFilter.as_view(), name='filter'),
    path('add_rating/', AddStarRating.as_view(), name='add_rating'),
    path('<slug:slug>/', GameDetailView.as_view(), name='game_detail'),
    path('review/<int:pk>/', AddReview.as_view(), name='add_review'),
    path('company/<str:slug>/', CompanyView.as_view(), name='company_detail'),

]
