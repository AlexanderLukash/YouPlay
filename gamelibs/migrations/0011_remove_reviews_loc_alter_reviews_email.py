# Generated by Django 4.0.6 on 2022-07-22 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamelibs', '0010_reviews_alter_profile_about_alter_profile_country_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviews',
            name='loc',
        ),
        migrations.AlterField(
            model_name='reviews',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Електронна пошта'),
        ),
    ]