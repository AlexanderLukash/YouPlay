from django import template
from ..models import *

register = template.Library()


@register.simple_tag()
def get_ganres():
    return Ganre.objects.all()


@register.simple_tag()
def get_categories():
    return Category.objects.all()


@register.simple_tag()
def get_tags():
    return Tags.objects.all()


@register.filter()
def class_name(value):
    return value.__class__.__name__


@register.filter(name='has_group')
def has_group(user, group_name):
    return user.groups.filter(name=group_name).exists()


@register.inclusion_tag('gamelibs/tags/randon_game_intro.html')
def get_random_games_intro():
    games = Game.objects.order_by('?').filter(draft=False)[:1]
    return {"get_random_games_intro": games}


@register.inclusion_tag('gamelibs/tags/randon_game_store.html')
def randon_game_store():
    games = Game.objects.order_by('?').filter(draft=False)[:5]
    return {"randon_game_store": games}


@register.inclusion_tag('gamelibs/tags/randon_game_slider.html')
def get_random_games_for_slider():
    games = Game.objects.order_by('?').filter(draft=False)[:15]
    return {"get_random_games_for_slider": games}


@register.inclusion_tag('gamelibs/tags/get_sale_games_for_slider.html')
def get_sale_games_for_slider():
    games = Game.objects.order_by('?').filter(sale_price__gt=0).filter(draft=False)[:15]
    return {"get_sale_games_for_slider": games}


@register.inclusion_tag('gamelibs/tags/get_last_games_for_slider.html')
def get_last_games_for_slider():
    games = Game.objects.order_by('-id').filter(draft=False)[:15]
    return {"get_last_games_for_slider": games}


@register.inclusion_tag('gamelibs/tags/get_popular_game_for_slider.html')
def get_popular_game_for_slider():
    games = Game.objects.order_by('-hit_count_generic__hits')[:15]
    return {"get_popular_game_for_slider": games}


@register.inclusion_tag('gamelibs/tags/get_random_game_for_main_page.html')
def get_random_game_for_main_page():
    games = Game.objects.order_by('?').filter(draft=False)[:1]
    return {"get_random_game_for_main_page": games}


@register.inclusion_tag('gamelibs/tags/get_last_post_for_main_page.html')
def get_last_post_for_main_page():
    posts = Post.objects.order_by('-id').filter(draft=False)
    return {"get_last_post_for_main_page": posts}


@register.inclusion_tag('gamelibs/tags/get_popular_game_for_sidebar.html')
def get_popular_game_for_sidebar():
    games = Game.objects.order_by('-hit_count_generic__hits')[:5]
    return {"get_popular_game_for_sidebar": games}


@register.simple_tag()
def get_popular_game_for_store():
    games = Game.objects.order_by('-hit_count_generic__hits')
    return {"get_popular_game_for_store": games}


@register.inclusion_tag('gamelibs/tags/get_popular_post_for_sidebar.html')
def get_popular_post_for_sidebar():
    posts = Post.objects.order_by('-hit_count_generic__hits').filter(draft=False)[:5]
    return {"get_popular_post_for_sidebar": posts}
