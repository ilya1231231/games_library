# Generated by Django 3.2.6 on 2021-08-18 17:00

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Категория')),
                ('description', models.TextField(verbose_name='Описание')),
                ('url', models.SlugField(max_length=160, unique=True)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название компании')),
                ('year', models.PositiveIntegerField(default=0, verbose_name='Год основания')),
                ('description', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(upload_to='companies', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Компания-разработчик',
                'verbose_name_plural': 'Компании-разработчики',
            },
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=160, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('poster', models.ImageField(upload_to='games/', verbose_name='Постер')),
                ('year', models.PositiveIntegerField(default=2000, verbose_name='Дата выхода')),
                ('country', models.CharField(max_length=160, verbose_name='Страна разработчик')),
                ('release_date', models.DateField(default=datetime.date.today, verbose_name='Дата выхода')),
                ('url', models.SlugField(max_length=160, unique=True)),
                ('draft', models.BooleanField(default=False, verbose_name='Черновик')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='games.category', verbose_name='Категория')),
                ('company', models.ManyToManyField(to='games.Company', verbose_name='Компания разработчик')),
            ],
            options={
                'verbose_name': 'Игра',
                'verbose_name_plural': 'Игры',
            },
        ),
        migrations.CreateModel(
            name='GamePlatform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('XBOX 360', 'XBOX 360'), ('XBOX One', 'XBOX One'), ('Playstation 4', 'Playstation 4'), ('Playstation 5', 'Playstation 5'), ('PC', 'PC'), ('Nintendo', 'Nintendo')], default='Playstation 4', max_length=160, verbose_name='Название платформы')),
                ('url', models.SlugField(max_length=160, unique=True)),
            ],
            options={
                'verbose_name': 'Игровая платформа',
                'verbose_name_plural': 'Игрорвые платформы',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('RPG', 'RPG'), ('Shooter', 'Shooter'), ('Fighting', 'Fighting'), ('Arcade', 'Arcade'), ('Strategy', 'Strategy'), ('Adventure', 'Adventure')], default='RPG', max_length=160, verbose_name='Название жанра')),
                ('description', models.TextField(verbose_name='Описание')),
                ('url', models.SlugField(max_length=160, unique=True)),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанры',
            },
        ),
        migrations.CreateModel(
            name='RatingStar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.SmallIntegerField(default=0, verbose_name='Значение')),
            ],
            options={
                'verbose_name': 'Звезда рейтинга',
                'verbose_name_plural': 'Звезды рейтинга',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=160, verbose_name='Имя')),
                ('text', models.TextField(max_length=5000, verbose_name='Сообщение')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.game', verbose_name='Игра')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='games.review', verbose_name='Родитель')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=15, verbose_name='IP')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.game', verbose_name='Игра')),
                ('star', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.ratingstar', verbose_name='Звезда')),
            ],
            options={
                'verbose_name': 'Звезда рейтинга',
                'verbose_name_plural': 'Звезды рейтинга',
            },
        ),
        migrations.CreateModel(
            name='GameScreenShoots',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=160, verbose_name='Заголовок')),
                ('description', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(upload_to='screen_shoots/', verbose_name='Изображение')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.game', verbose_name='Игра')),
            ],
            options={
                'verbose_name': 'Скриншот из игры',
                'verbose_name_plural': 'Скриншоты из игры',
            },
        ),
        migrations.AddField(
            model_name='game',
            name='game_platform',
            field=models.ManyToManyField(to='games.GamePlatform', verbose_name='Игровая платформа'),
        ),
        migrations.AddField(
            model_name='game',
            name='genre',
            field=models.ManyToManyField(to='games.Genre', verbose_name='Жанры игры'),
        ),
    ]
