# Generated by Django 3.0.11 on 2021-01-07 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('_blog', '0016_auto_20210107_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='fb_link',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='ist_link',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='tw_link',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
