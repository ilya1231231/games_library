from django.db import models
from datetime import date

from django.urls import reverse


class Category(models.Model):
    '''Категории игр'''
    name = models.CharField('Категория', max_length=150)
    description = models.TextField('Описание')
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Company(models.Model):
    '''Компания-разработчик'''
    name = models.CharField('Название компании', max_length=150)
    year = models.PositiveIntegerField('Год основания', default=0)
    description = models.TextField('Описание')
    image = models.ImageField('Изображение', upload_to='companies')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Компания-разработчик'
        verbose_name_plural = 'Компании-разработчики'


class Genre(models.Model):
    '''Жанр игры'''
    GENRE_RPG = 'RPG'
    GENRE_SHOOTER = 'Shooter'
    GENRE_FIGHTING = 'Fighting'
    GENRE_ARCADE = 'Arcade'
    GENRE_STRATEGY = 'Strategy'
    GENRE_ADVENTURE = 'Adventure'

    GENRE_CHOICES = (
        (GENRE_RPG, 'RPG'),
        (GENRE_SHOOTER, 'Shooter'),
        (GENRE_FIGHTING, 'Fighting'),
        (GENRE_ARCADE, 'Arcade'),
        (GENRE_STRATEGY, 'Strategy'),
        (GENRE_ADVENTURE, 'Adventure')
    )

    name = models.CharField('Название жанра', max_length=160, choices=GENRE_CHOICES, default=GENRE_RPG)
    description = models.TextField('Описание')
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class GamePlatform(models.Model):
    '''Игровая платформа'''
    GAME_PLATFORM_XBOX360 = 'XBOX 360'
    GAME_PLATFORM_XBOX_ONE = 'XBOX One'
    GAME_PLATFORM_PS4 = 'Playstation 4'
    GAME_PLATFORM_PS5 = 'Playstation 5'
    GAME_PLATFORM_PC = 'PC'
    GAME_PLATFORM_NINTENDO = 'Nintendo'

    GAME_PLATFORM_CHOICES = (
        (GAME_PLATFORM_XBOX360, 'XBOX 360'),
        (GAME_PLATFORM_XBOX_ONE, 'XBOX One'),
        (GAME_PLATFORM_PS4, 'Playstation 4'),
        (GAME_PLATFORM_PS5, 'Playstation 5'),
        (GAME_PLATFORM_PC, 'PC'),
        (GAME_PLATFORM_NINTENDO, 'Nintendo')
    )

    name = models.CharField(
        'Название платформы', max_length=160, choices=GAME_PLATFORM_CHOICES, default=GAME_PLATFORM_PS4
    )
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Игровая платформа'
        verbose_name_plural = 'Игрорвые платформы'




class Game(models.Model):
    '''Игра'''
    title = models.CharField('Название', max_length=160)
    description = models.TextField('Описание')
    poster = models.ImageField('Постер', upload_to='games/')
    year = models.PositiveIntegerField('Дата выхода', default=2000)
    country = models.CharField('Страна разработчик', max_length=160)
    release_date = models.DateField('Дата выхода', default=date.today)
    company = models.ManyToManyField(Company, verbose_name='Компания разработчик')
    genre = models.ManyToManyField(Genre, verbose_name='Жанры игры')
    game_platform = models.ManyToManyField(GamePlatform, verbose_name='Игровая платформа')
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.SET_NULL, null=True)
    url = models.SlugField(max_length=160, unique=True)
    draft = models.BooleanField('Черновик', default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('game_detail', kwargs={'slug': self.url})

    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'


class GameScreenShoots(models.Model):
    '''Скриншоты из игры'''
    title = models.CharField('Заголовок', max_length=160)
    description = models.TextField('Описание')
    image = models.ImageField('Изображение', upload_to='screen_shoots/')
    game = models.ForeignKey(Game, verbose_name='Игра', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Скриншот из игры'
        verbose_name_plural = 'Скриншоты из игры'


class RatingStar(models.Model):
    '''Звезды рейтинга'''
    value = models.SmallIntegerField('Значение', default=0)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = 'Звезда рейтинга'
        verbose_name_plural = 'Звезды рейтинга'


class Rating(models.Model):
    '''Рейтинг'''
    ip = models.CharField('IP', max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name='Звезда')
    game = models.ForeignKey(Game, on_delete=models.CASCADE, verbose_name='Игра')

    def __str__(self):
        return '{} - {}'.format(self.star, self.game)

    class Meta:
        verbose_name = 'Звезда рейтинга'
        verbose_name_plural = 'Звезды рейтинга'


class Review(models.Model):
    '''Отзыв'''
    email = models.EmailField()
    name = models.CharField('Имя', max_length=160)
    text = models.TextField('Сообщение', max_length=5000)
    parent = models.ForeignKey(
        'self', verbose_name='Родитель', on_delete=models.SET_NULL, blank=True, null=True
    )
    game = models.ForeignKey(Game, verbose_name='Игра', on_delete=models.CASCADE)

    def __str__(self):
        return '{} - {}'.format(self.name, self.game)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'