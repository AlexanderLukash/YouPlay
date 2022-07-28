from django.contrib import admin
from django import forms
from django.utils.safestring import mark_safe
from .models import Category, Ganre, Company, Game, GameShots, Post, Tags, Good, Bad, Profile, GameReview, PostReview, \
    ReviewContact
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class GameAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Game
        fields = '__all__'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "url")
    list_display_links = ("name",)


class GameShotsInline(admin.TabularInline):
    model = GameShots
    extra = 0
    readonly_fields = ("get_full_image",)

    def get_full_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="200" height="110"')

    get_full_image.short_description = "Зображення"


@admin.register(Ganre)
class GanreAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "url")
    list_display_links = ("name",)


@admin.register(Company)
class Company(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("name",)


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "url", "draft")
    list_display_links = ("title",)
    list_filter = ("category", "ganres")
    search_fields = ("title", "category__name")
    inlines = [GameShotsInline]
    save_on_top = True
    save_as = True
    form = GameAdminForm
    actions = ["published", "unpublished"]
    list_editable = ("draft",)

    def unpublished(self, request, queryset):
        row_update = queryset.update(draft=True)
        if row_update == 1:
            message_bit = "1 запис був оновлений."
        else:
            message_bit = f"{row_update} записів було оновлено."
        self.message_user(request, f"{message_bit}")

    def published(self, request, queryset):
        row_update = queryset.update(draft=False)
        if row_update == 1:
            message_bit = "1 запис був опублікований."
        else:
            message_bit = f"{row_update} записів було опубліковано."
        self.message_user(request, f"{message_bit}")

    published.short_description = "Опублікувати"
    published.allowed_permissions = ("change",)
    unpublished.short_description = "Зняти з публікації"
    unpublished.allowed_permissions = ("change",)


@admin.register(GameShots)
class MovieShotsAdmin(admin.ModelAdmin):
    list_display = ("title", "game", "get_image",)
    readonly_fields = ("get_full_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="70" height="40"')

    def get_full_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="200" height="110"')

    get_image.short_description = "Зображення"
    get_full_image.short_description = "Зображення"


@admin.register(Post)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "rank", "draft")
    list_display_links = ("title",)
    search_fields = ("title", "category__name")
    save_on_top = True
    save_as = True
    form = GameAdminForm
    actions = ["published", "unpublished"]
    list_editable = ("draft",)

    def unpublished(self, request, queryset):
        row_update = queryset.update(draft=True)
        if row_update == 1:
            message_bit = "1 запис був оновлений."
        else:
            message_bit = f"{row_update} записів було оновлено."
        self.message_user(request, f"{message_bit}")

    def published(self, request, queryset):
        row_update = queryset.update(draft=False)
        if row_update == 1:
            message_bit = "1 запис був опублікований."
        else:
            message_bit = f"{row_update} записів було опубліковано."
        self.message_user(request, f"{message_bit}")

    published.short_description = "Опублікувати"
    published.allowed_permissions = ("change",)
    unpublished.short_description = "Зняти з публікації"
    unpublished.allowed_permissions = ("change",)


@admin.register(Tags)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "url")
    list_display_links = ("title",)


@admin.register(Good)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "url")
    list_display_links = ("title",)


@admin.register(Bad)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "url")
    list_display_links = ("title",)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("id", "user")
    list_display_links = ("user",)


@admin.register(GameReview)
class GameReview(admin.ModelAdmin):
    list_display = ("id", "user", "game", "date")
    list_display_links = ("user",)


@admin.register(PostReview)
class PostReview(admin.ModelAdmin):
    list_display = ("id", "user", "post", "date")
    list_display_links = ("user",)


@admin.register(ReviewContact)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email",)
    list_display_links = ("name",)
