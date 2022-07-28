# Generated by Django 4.0.6 on 2022-07-23 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamelibs', '0012_remove_post_games_post_games'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='games',
        ),
        migrations.AddField(
            model_name='post',
            name='games',
            field=models.ManyToManyField(help_text='Вказати тільки одну гру!', related_name='games', to='gamelibs.game', verbose_name='Вкажіть гру'),
        ),
    ]
