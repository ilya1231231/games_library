from django.contrib import admin
from .models import (
    Category,
    Company,
    Genre,
    GamePlatform,
    Game,
    GameScreenShoots,
    RatingStar,
    Rating,
    Review
)


class ReviewInLine(admin.StackedInline):  # Класс для отображения отзыва в игре
    model = Review
    extra = 1  # Указываю количество пустых полей
    readonly_fields = ('name', 'email')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url')  # Последовательность отображения полей
    list_display_links = ('name',)  # Делаю ссылку на поле name для детального просмотра категории


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url', 'draft')
    list_filter = ('category', 'year')  # Фильтрация по полю
    search_fields = ('title',)  # Поиск по названию игры
    inlines = [ReviewInLine]  # Добавляю класс для отображения отзыва во вкладке игры
    save_on_top = True  # Кнопки сохранения и удаления оставляем наверху
    save_as = True  # Функция сохранения как нового объекта
    list_editable = ('draft', )  # Добавил чекбокс для удобного сохранения в черновик
    '''Группировка полей для удобной работы'''
    fieldsets = (
        (None, {
            'fields': (('title', ), )
        }),
        ('Описание и постер игры', {
            'fields': (('description', 'poster'), )
        }),
        ('Даты выпуска', {
            'fields': (('year', 'country', 'release_date'), )
        }),
        ('Компании, игровые платформы, жанры, категории', {
            'classes': ('collapse', ),  # Функция для сокращения столбца
            'fields': (('company', 'game_platform', 'genre', 'category'), )
        }),
        ('Опции', {
            'fields': (('url', 'draft'), )
        }),
    )


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'text', 'parent', 'game', 'id')
    readonly_fields = ('name', 'email')  # Закрываю от редактирования указанные поля


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'year')


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')


@admin.register(GamePlatform)
class GamePlatformAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')


@admin.register(GameScreenShoots)
class GameScreenShootsAdmin(admin.ModelAdmin):
    list_display = ('title', 'game')


@admin.register(RatingStar)
class RatingStarAdmin(admin.ModelAdmin):
    list_display = ('value',)


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('ip', 'star', 'game')

