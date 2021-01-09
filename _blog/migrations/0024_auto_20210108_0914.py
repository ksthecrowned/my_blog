# Generated by Django 3.0.11 on 2021-01-08 08:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('_blog', '0023_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='author',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]