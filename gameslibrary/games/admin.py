from django.contrib import admin
from django.utils.safestring import mark_safe
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

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


class GameAdminForm(forms.ModelForm):  # Подключаю CKeditor
    description = forms.CharField(label='Описание',
        widget=CKEditorUploadingWidget())  # В качестве поля формы выбрал описание из модели Game

    class Meta:
        model = Game
        fields = '__all__'


class ReviewInLine(admin.TabularInline):  # Класс для отображения отзыва в игре
    model = Review
    extra = 1  # Указываю количество пустых полей
    readonly_fields = ('name', 'email')


class GameScreenShootsInLine(admin.TabularInline):  # Отображение скриншотов в дитейле игры
    model = GameScreenShoots
    extra = 1
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(
            f'<img src={obj.image.url} width="100" height="auto"')  # mark_safe с f строкой для отображения в админке

    get_image.short_description = 'Изображение'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url')  # Последовательность отображения полей
    list_display_links = ('name',)  # Делаю ссылку на поле name для детального просмотра категории


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url', 'draft')
    list_filter = ('category', 'year')  # Фильтрация по полю
    search_fields = ('title',)  # Поиск по названию игры
    inlines = [GameScreenShootsInLine, ReviewInLine]  # Добавляю класс для отображения отзыва,скриншота во вкладке игры
    save_on_top = True  # Кнопки сохранения и удаления оставляем наверху
    save_as = True  # Функция сохранения как нового объекта
    list_editable = ('draft',)  # Добавил чекбокс для удобного сохранения в черновик
    readonly_fields = ('get_image',)
    form = GameAdminForm
    '''Группировка полей для удобной работы'''
    fieldsets = (
        (None, {
            'fields': (('title',),)
        }),
        ('Описание и постер игры', {
            'fields': (('description', 'get_image'),)
        }),
        ('Даты выпуска', {
            'fields': (('year', 'country', 'release_date'),)
        }),
        ('Компании, игровые платформы, жанры, категории', {
            'classes': ('collapse',),  # Функция для сокращения столбца
            'fields': (('company', 'game_platform', 'genre', 'category'),)
        }),
        ('Опции', {
            'fields': (('url', 'draft'),)
        }),
    )

    def get_image(self, obj):
        return mark_safe(
            f'<img src={obj.poster.url} width="150" height="auto"')  # mark_safe с f строкой для отображения в админке

    get_image.short_description = 'Постер игры'


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'text', 'parent', 'game', 'id')
    readonly_fields = ('name', 'email')  # Закрываю от редактирования указанные поля


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'year', 'get_image')  # Имя метода указанного ниже
    readonly_fields = ('get_image',)  # Для отображения в дитейле при открытии

    def get_image(self, obj):
        return mark_safe(
            f'<img src={obj.image.url} width="100" height="auto"')  # mark_safe с f строкой для отображения в админке

    get_image.short_description = 'Изображение'


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')


@admin.register(GamePlatform)
class GamePlatformAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')


@admin.register(GameScreenShoots)
class GameScreenShootsAdmin(admin.ModelAdmin):
    list_display = ('title', 'game', 'get_image')
    readonly_fields = ('get_image',)  # Для отображения в дитейле при открытии

    def get_image(self, obj):
        return mark_safe(
            f'<img src={obj.image.url} width="70" height="auto"')  # mark_safe с f строкой для отображения в админке

    get_image.short_description = 'Изображение'


@admin.register(RatingStar)
class RatingStarAdmin(admin.ModelAdmin):
    list_display = ('value',)


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('ip', 'star', 'game')


admin.site.site_title = 'Игровая библиотека'  # Меняем название
admin.site.site_header = 'Игровая библиотека'
