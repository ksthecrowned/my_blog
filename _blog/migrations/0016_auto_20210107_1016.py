# Generated by Django 3.0.11 on 2021-01-07 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('_blog', '0015_author_facebook'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='facebook',
            new_name='fb_link',
        ),
        migrations.AddField(
            model_name='author',
            name='ist_link',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='author',
            name='tw_link',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
