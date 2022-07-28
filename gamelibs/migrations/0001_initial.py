# Generated by Django 4.0.6 on 2022-07-20 10:15

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('url', models.SlugField(max_length=160, unique=True)),
            ],
            options={
                'verbose_name': 'Негатив',
                'verbose_name_plural': 'Негативні',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Назва')),
                ('url', models.SlugField(max_length=160, unique=True)),
            ],
            options={
                'verbose_name': 'Категорія',
                'verbose_name_plural': 'Категорії',
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Назва')),
                ('description', models.TextField(verbose_name='Описання')),
                ('image', models.ImageField(upload_to='company/img/image', verbose_name='Зображення')),
            ],
            options={
                'verbose_name': 'Компанії',
                'verbose_name_plural': 'Компанії',
            },
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Назва')),
                ('tagline', models.CharField(default='', max_length=500, verbose_name='Слоган')),
                ('description', models.TextField(verbose_name='Описання')),
                ('description_small', models.CharField(max_length=100, null=True, verbose_name='Описання коротко')),
                ('poster', models.ImageField(upload_to='games/poster/', verbose_name='Постер')),
                ('banner', models.ImageField(null=True, upload_to='games/banner/', verbose_name='Банер')),
                ('treiler', models.CharField(max_length=500, null=True, verbose_name='Трейлер')),
                ('treiler_img', models.ImageField(null=True, upload_to='games/intro/', verbose_name='Інтро терейлеру')),
                ('country', models.CharField(max_length=30, verbose_name='Країна')),
                ('price', models.FloatField(help_text='У форматі 10.00', max_length=100, verbose_name='Ціна')),
                ('sale_price', models.IntegerField(blank=True, default=0, verbose_name='Скидка в процентах')),
                ('world_premiere', models.DateField(default=datetime.date.today, verbose_name='Дата виходу')),
                ('budget', models.PositiveIntegerField(default=0, help_text='вказуйте сумму в доларах.', verbose_name='Бюджет')),
                ('url', models.SlugField(max_length=255, unique=True)),
                ('os', models.CharField(max_length=100, verbose_name='Операційні системи')),
                ('processor', models.CharField(max_length=100, verbose_name='Процесор')),
                ('memory', models.CharField(max_length=100, verbose_name='Операційна памьять')),
                ('graphics', models.CharField(max_length=100, verbose_name='Відеокарта')),
                ('hard_drive', models.CharField(max_length=100, verbose_name='Місце на диску')),
                ('draft', models.BooleanField(default=False, verbose_name='Чернетка')),
                ('category', models.ManyToManyField(to='gamelibs.category', verbose_name='Категорія')),
                ('company', models.ManyToManyField(related_name='company_game', to='gamelibs.company', verbose_name='Компанія')),
            ],
            options={
                'verbose_name': 'Гра',
                'verbose_name_plural': 'Ігри',
            },
        ),
        migrations.CreateModel(
            name='Ganre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Назва')),
                ('url', models.SlugField(max_length=160, unique=True)),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанри',
            },
        ),
        migrations.CreateModel(
            name='Good',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('url', models.SlugField(max_length=160, unique=True)),
            ],
            options={
                'verbose_name': 'Позитив',
                'verbose_name_plural': 'Позитивні',
            },
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('url', models.SlugField(max_length=160, unique=True)),
            ],
            options={
                'verbose_name': 'Тег',
                'verbose_name_plural': 'Теги',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(default='../static/avatar_default.png', upload_to='profile/avatar/', verbose_name='Аватар користувача')),
                ('town', models.CharField(max_length=100, null=True, verbose_name='Місто')),
                ('country', models.CharField(max_length=100, null=True, verbose_name='Країна')),
                ('phone_number', models.IntegerField(null=True, verbose_name='Номер телефону')),
                ('email', models.EmailField(max_length=254, null=True, verbose_name='Електронна пошта')),
                ('github', models.CharField(max_length=100, null=True, verbose_name='Профіль GitHub')),
                ('about', models.TextField(null=True, verbose_name='Про користувача')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Профіль',
                'verbose_name_plural': 'Профілі',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('foreword_description', models.TextField(max_length=335, verbose_name='Передмова')),
                ('description', models.TextField(verbose_name='Описання')),
                ('rank', models.FloatField(default=0, help_text='Від 1 до 10', verbose_name='Оцінка')),
                ('premiere', models.DateField(default=datetime.date.today, verbose_name='Дата публікації')),
                ('url', models.SlugField(default='Введіть унікальний аудентифікатор', max_length=255, unique=True)),
                ('draft', models.BooleanField(default=False, verbose_name='Чернетка')),
                ('bad', models.ManyToManyField(help_text='Максимальна кількість 4', to='gamelibs.bad', verbose_name='Негативні речі')),
                ('games', models.ManyToManyField(help_text='Вказати тільки одну гру!', related_name='games', to='gamelibs.game', verbose_name='Вкажіть гру')),
                ('good', models.ManyToManyField(help_text='Максимальна кількість 4', to='gamelibs.good', verbose_name='Позитивні речі')),
                ('tags', models.ManyToManyField(help_text='Вказати тільки 4 тега!', to='gamelibs.tags', verbose_name='Теги')),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Пости',
            },
        ),
        migrations.CreateModel(
            name='GameShots',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('image', models.ImageField(upload_to='movie_shots/', verbose_name='Зображення')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gamelibs.game', verbose_name='Гра')),
            ],
            options={
                'verbose_name': 'Кадр із гри',
                'verbose_name_plural': 'Кадри з гри',
            },
        ),
        migrations.CreateModel(
            name='GameReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Описання')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gamelibs.game', verbose_name='Гра')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Ігровий відгук',
                'verbose_name_plural': 'Ігрові відгуки',
            },
        ),
        migrations.AddField(
            model_name='game',
            name='ganres',
            field=models.ManyToManyField(to='gamelibs.ganre', verbose_name='Жанри'),
        ),
    ]
