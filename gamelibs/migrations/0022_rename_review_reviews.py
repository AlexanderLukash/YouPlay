# Generated by Django 4.0.6 on 2022-07-28 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gamelibs', '0021_rename_reviews_review'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Review',
            new_name='Reviews',
        ),
    ]
