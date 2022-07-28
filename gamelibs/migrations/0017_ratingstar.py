# Generated by Django 4.0.6 on 2022-07-28 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamelibs', '0016_remove_game_budget_remove_game_description_small'),
    ]

    operations = [
        migrations.CreateModel(
            name='RatingStar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.SmallIntegerField(default=0, verbose_name='Значення')),
            ],
            options={
                'verbose_name': 'Зірка Рейтингу',
                'verbose_name_plural': 'Зірки Рейтингу',
                'ordering': ['-value'],
            },
        ),
    ]
