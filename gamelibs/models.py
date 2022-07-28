from django.contrib.auth.models import User
from django.db import models
from datetime import date

from django.db.models import Q
from django.urls import reverse
from django.dispatch import receiver
from django.db.models.signals import post_save
from hitcount.models import HitCountMixin, HitCount
from django.contrib.contenttypes.fields import GenericRelation


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField('Аватар користувача', upload_to="profile/avatar/",
                               default="../static/avatar_default.png")
    town = models.CharField('Місто', max_length=100, null=True, blank=True)
    country = models.CharField('Країна', max_length=100, null=True, blank=True)
    phone_number = models.IntegerField('Номер телефону', null=True, blank=True)
    email = models.EmailField('Електронна пошта', null=True, blank=True)
    github = models.CharField('Профіль GitHub', max_length=100, null=True, blank=True)
    about = models.TextField('Про користувача', null=True, blank=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse("user_profile", kwargs={"slug": self.user_id})

    @receiver(post_save, sender=User)  # add this
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)  # add this
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    class Meta:
        verbose_name = "Профіль"
        verbose_name_plural = "Профілі"


class Tags(models.Model):
    title = models.CharField("Заголовок", max_length=100)
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("tag_filter", kwargs={"slug": self.url})

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"


class Good(models.Model):
    title = models.CharField("Заголовок", max_length=100)
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("good_blog_filter", kwargs={"slug": self.url})

    class Meta:
        verbose_name = "Позитив"
        verbose_name_plural = "Позитивні"


class Bad(models.Model):
    title = models.CharField("Заголовок", max_length=100)
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("bad_blog_filter", kwargs={"slug": self.url})

    class Meta:
        verbose_name = "Негатив"
        verbose_name_plural = "Негативні"


class Category(models.Model):
    name = models.CharField("Назва", max_length=150)
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("category_filter", kwargs={"slug": self.url})

    class Meta:
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"


class Ganre(models.Model):
    name = models.CharField("Назва", max_length=100)
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("ganre_filter", kwargs={"slug": self.url})

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанри"


class Company(models.Model):
    name = models.CharField("Назва", max_length=100)
    description = models.TextField("Описання")
    image = models.ImageField("Зображення", upload_to="company/img/image")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("company_details", kwargs={"slug": self.name})

    class Meta:
        verbose_name = "Компанії"
        verbose_name_plural = "Компанії"


class GameManager(models.Manager):
    def search(self, query=None):
        qs = self.get_queryset()
        if query is not None:
            or_lookup = (Q(title__icontains=query))
            qs = qs.filter(or_lookup).distinct()  # distinct() is often necessary with Q lookups
        return qs


class Game(models.Model):
    title = models.CharField("Назва", max_length=100)
    tagline = models.CharField("Слоган", max_length=500, default='')
    description = models.TextField("Описання")
    poster = models.ImageField("Постер", upload_to="games/poster/")
    banner = models.ImageField("Банер", upload_to="games/banner/", null=True)
    treiler = models.CharField("Трейлер", max_length=500, null=True)
    treiler_img = models.ImageField("Інтро терейлеру", upload_to="games/intro/", null=True)
    country = models.CharField("Країна", max_length=30)
    company = models.ManyToManyField(Company, verbose_name="Компанія", related_name="company_game")
    ganres = models.ManyToManyField(Ganre, verbose_name="Жанри")
    price = models.FloatField("Ціна", help_text="У форматі 10.00", max_length=100)
    sale_price = models.IntegerField('Скидка в процентах', blank=True, default=0)
    world_premiere = models.DateField("Дата виходу", default=date.today)
    category = models.ManyToManyField(Category, verbose_name="Категорія")
    url = models.SlugField(max_length=255, unique=True)
    os = models.CharField("Операційні системи", max_length=100)
    processor = models.CharField("Процесор", max_length=100)
    memory = models.CharField("Операційна памьять", max_length=100)
    graphics = models.CharField("Відеокарта", max_length=100)
    hard_drive = models.CharField("Місце на диску", max_length=100)
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk',
                                        related_query_name='hit_count_generic_relation', default=0)
    draft = models.BooleanField("Чернетка", default=False)
    objects = GameManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("game_details", kwargs={"slug": self.url})

    def get_sale(self):
        if self.sale_price == 100:
            return 'FREE'
        elif self.sale_price == 0:
            return f'{self.price}'
        else:
            price = float(self.price * (100 - self.sale_price) / 100)
            x = float('{:.2f}'.format(price))
            return x

    def get_cart_sale(self):
        if self.sale_price == 100:
            return '00.00'
        elif self.sale_price == 0:
            return f'{self.price}'
        else:
            price = float(self.price * (100 - self.sale_price) / 100)
            x = float('{:.2f}'.format(price))
            return x

    class Meta:
        verbose_name = "Гра"
        verbose_name_plural = "Ігри"


class GameReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    game = models.ForeignKey(Game, verbose_name="Гра", on_delete=models.CASCADE)
    text = models.TextField("Описання")
    date = models.DateField("Дата публікації", default=date.today)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ["-id"]
        verbose_name = "Ігровий відгук"
        verbose_name_plural = "Ігрові відгуки"


class GameShots(models.Model):
    title = models.CharField("Заголовок", max_length=100)
    image = models.ImageField("Зображення", upload_to="movie_shots/")
    game = models.ForeignKey(Game, verbose_name="Гра", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Кадр із гри"
        verbose_name_plural = "Кадри з гри"


class PostManager(models.Manager):
    def search(self, query=None):
        qs = self.get_queryset()
        if query is not None:
            or_lookup = (Q(title__icontains=query))
            qs = qs.filter(or_lookup).distinct()  # distinct() is often necessary with Q lookups
        return qs


class Post(models.Model):
    title = models.CharField("Заголовок", max_length=100)
    games = models.ManyToManyField(Game, verbose_name="Вкажіть гру", help_text="Вказати тільки одну гру!",
                                   related_name='games')
    tags = models.ManyToManyField(Tags, verbose_name="Теги", help_text="Вказати тільки 4 тега!")
    foreword_description = models.TextField("Передмова", max_length=335)
    description = models.TextField("Описання")
    rank = models.FloatField("Оцінка", default=0, help_text="Від 1 до 10")
    good = models.ManyToManyField(Good, verbose_name="Позитивні речі", help_text="Максимальна кількість 4")
    bad = models.ManyToManyField(Bad, verbose_name="Негативні речі", help_text="Максимальна кількість 4")
    premiere = models.DateField("Дата публікації", default=date.today)
    url = models.SlugField(max_length=255, unique=True, default="Введіть унікальний аудентифікатор")
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk',
                                        related_query_name='hit_count_generic_relation')
    draft = models.BooleanField("Чернетка", default=False)
    objects = PostManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_details", kwargs={"slug": self.url})

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Пости"


class PostReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    post = models.ForeignKey(Post, verbose_name="Гра", on_delete=models.CASCADE)
    text = models.TextField("Описання")
    date = models.DateField("Дата публікації", default=date.today)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ["-id"]
        verbose_name = "Відгук поста"
        verbose_name_plural = "Відгуки постів"


class ReviewContact(models.Model):
    email = models.EmailField('Електронна пошта')
    name = models.CharField("Ім'я", max_length=100)
    text = models.TextField("Повідомлення", max_length=200)
    draft = models.BooleanField("Чернетка", default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Відгук"
        verbose_name_plural = "Відгуки"


