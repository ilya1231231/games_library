from django import forms
from .models import Review, Rating, RatingStar


class ReviewForm(forms.ModelForm):
    '''Форма отзыва'''

    class Meta:
        model = Review
        fields = ('name', 'email', 'text')


class RatingForm(forms.ModelForm):
    '''Форма для добавления рейтинга '''
    star = forms.ModelChoiceField(
        queryset=RatingStar.objects.all(), widget=forms.RadioSelect(), empty_label=None
    )
    '''Переопределяю только поле star'''
    class Meta:
        model = Rating
        fields = ('star',)

